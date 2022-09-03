# %%
import yfinance as yf
import pandas as pd
import numpy as np
import pickle

# %%
# S&P 500 公司：全美最高金额买卖的500只股票
# 阶段目标：1. 根据公司的sector为其数据打上标签，做分类；2. 查看每个类别数量，做特征（asset）挑选；

asset_list = pd.read_csv('./rawData/dailyStockPrice-5Y/SP500assets.csv')
# asset_list含三个属性：symbol(公司简称)， name（公司全称），sector(公司领域)

# 验证公司是否是美国的（划去，意义不大）
# for i in range(asset_list.shape[0]):
#     asset = asset_list['Symbol'][i]
#     al = yf.Ticker(asset)
#     cominfo = al.info
#     if cominfo['country'] != 'United States':
#         print(cominfo['country'] )
#         asset_list = asset_list.drop(labels=i)

# 创建字典，将symbol作为key，sector作为value
asset_dict = dict(zip(asset_list['Symbol'], asset_list['Sector']))
with open('./rawData/dailyStockPrice-5Y/categoryOfAssets.pkl', 'wb') as tf:
    pickle.dump(asset_dict, tf)

# 统计所有类别，及每个类别的asset数量
category = set(asset_dict.values())

def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

for element in category:
    print(element, len(get_key(asset_dict, element)))

# Utilities 28
# Consumer Staples 34
# Telecommunication Services 3
# Industrials 67
# Health Care 61
# Materials 25
# Real Estate 33
# Consumer Discretionary 84
# Energy 32
# Information Technology 70
# Financials 68


# %%
# 暂且选取Health Care、Materials、Real Estate三种类别的公司作为特征/节点
# 阶段目标：1. 筛选特征；2. 提取特征20170901-20220901的五年每天的stock price作为5个数据集

features = get_key(asset_dict, 'Health Care') + get_key(asset_dict, 'Materials') + get_key(asset_dict, 'Real Estate')

# 提取每天close的股价
dates = ['2017-09-01', '2018-09-01', '2019-09-01', '2020-09-01', '2021-09-01', '2022-09-01']
for i in range(len(dates)-1):
    start_date = dates[i]
    end_date = dates[i+1]
    hist = yf.download(features, start=start_date, end=end_date)
    hist_close = hist['Close']
    filename = "./rawData/dailyStockPrice-5Y/raw" + start_date + 'to' + end_date + "stock_price_close.csv"
    hist_close.to_csv(filename, index_label='Date')

