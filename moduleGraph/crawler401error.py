# %%
import numpy as np
import time
from urllib.request import urlretrieve
import os

print(os.getcwd())

# %%

# 公司名称
assets = ['CSCO', 'BUD', 'BA', 'MDT', 'MO', 'C', 'T', 'WB', 'BAC', 'HAL',\
                 'F', 'PEP', 'MRK', 'S', 'ORCL', 'ETR', 'PG', 'TBT', 'CAT', 'MCD', \
                'EP', 'INTC', 'GM', 'TXN', 'MMM', 'IP', 'KO', 'UPS', 'EME', 'MSFT', \
                'DD', 'HPQ', 'EXC', 'HD', 'FDX', 'HIG', 'AXP', 'SO', 'XOM', 'CVX', \
                'CMCSA', 'ROK', 'NSC', 'TYCMY', 'RF', 'CCU', 'ATI', 'IBM', 'USB', 'WFC', \
                'GS', 'GD', 'DELL', 'DIS', 'GE', 'ALL', 'CVS', 'JPM', 'ABT', 'COF', \
                'TSLA', 'COP', 'NYXH', 'GOOG', 'PFE', 'CL', 'VZ', 'AMGN', 'BHIL', 'MS',\
                'CPB', 'BK', 'UNH', 'WMB', 'AIG', 'HON', 'AES', 'SLB', 'XRX', 'TGT', \
                'AAPL', 'WY', 'BAX', 'BMY', 'AA', 'AEP', 'CI', 'DOW', 'AVPT', 'JNJ']

start_date = '2017-09-01'
end_date = '2022-09-01'

# 将字符串格式化
start_array = time.strptime(start_date, "%Y-%m-%d")
end_array = time.strptime(end_date, "%Y-%m-%d")
# 将格式化的datetime转换成时间戳
start_stamp = int(time.mktime(start_array))
end_stamp = int(time.mktime(end_array))
print(start_stamp, end_stamp)

# %%
# 循环爬取数据
#循环爬取数据
for asset in assets:
    url = "https://query1.finance.yahoo.com/v7/finance/\download/"+asset+"?period1="+str(start_stamp)+"&period2\="+str(end_stamp)+"&interval=1d&events=history&includeAdjustedClose=true"
    filename = asset + '.csv'
    urlretrieve(url, filename)
    time.sleep(1)  


# %%
