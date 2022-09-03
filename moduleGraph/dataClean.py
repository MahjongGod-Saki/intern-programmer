# %%
import numpy as np
import pandas as pd
import os
print(os.getcwd())
# 导入raw data
first_year_data = pd.read_csv('./rawData/dailyStockPrice-5Y/raw2017-09-01to2018-09-01stock_price_close.csv')
second_year_data = pd.read_csv('./rawData/dailyStockPrice-5Y/raw2018-09-01to2019-09-01stock_price_close.csv')
third_year_data = pd.read_csv('./rawData/dailyStockPrice-5Y/raw2019-09-01to2020-09-01stock_price_close.csv')
fourth_year_data = pd.read_csv('./rawData/dailyStockPrice-5Y/raw2020-09-01to2021-09-01stock_price_close.csv')
fifth_year_data = pd.read_csv('./rawData/dailyStockPrice-5Y/raw2021-09-01to2022-09-01stock_price_close.csv')
print("====未清洗=====")
print("2017-09-01 to 2018-09-01, the shape of the dataset:", first_year_data.shape)
print("2018-09-01 to 2019-09-01, the shape of the dataset:", second_year_data.shape)
print("2019-09-01 to 2020-09-01, the shape of the dataset:", third_year_data.shape)
print("2020-09-01 to 2021-09-01, the shape of the dataset:", fourth_year_data.shape)
print("2021-09-01 to 2022-09-01, the shape of the dataset:", fifth_year_data.shape)

# %%
# 洗掉NAN数据

first_year_data = first_year_data.dropna(axis=1, how='any')
second_year_data = second_year_data.dropna(axis=1, how='any')
third_year_data = third_year_data.dropna(axis=1, how='any')
fourth_year_data = fourth_year_data.dropna(axis=1, how='any')
fifth_year_data = fifth_year_data.dropna(axis=1, how='any')

first_year_data = first_year_data.drop('Date', axis=1)
second_year_data = second_year_data.drop('Date', axis=1)
third_year_data = third_year_data.drop('Date', axis=1)
fourth_year_data = fourth_year_data.drop('Date', axis=1)
fifth_year_data = fifth_year_data.drop('Date', axis=1)
print("====清洗后=====")
print("2017-09-01 to 2018-09-01, the shape of the dataset:", first_year_data.shape)
print("2018-09-01 to 2019-09-01, the shape of the dataset:", second_year_data.shape)
print("2019-09-01 to 2020-09-01, the shape of the dataset:", third_year_data.shape)
print("2020-09-01 to 2021-09-01, the shape of the dataset:", fourth_year_data.shape)
print("2021-09-01 to 2022-09-01, the shape of the dataset:", fifth_year_data.shape)


# %%
# 提取五年数据共同的keys，作为features
features = list(set(first_year_data.keys()) & set(second_year_data.keys()) & set(third_year_data.keys()) & set(fourth_year_data.keys()) & set(fifth_year_data.keys()))

# 统一数据的feature，随后进行归一化，并计算协方差矩阵
first_year_data = first_year_data[features]
second_year_data = second_year_data[features]
third_year_data = third_year_data[features]
fourth_year_data = fourth_year_data[features]
fifth_year_data = fifth_year_data[features]


def nmlz(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

normalized_first_year_data = nmlz(first_year_data)
normalized_second_year_data = nmlz(second_year_data)
normalized_third_year_data = nmlz(third_year_data)
normalized_fourth_year_data = nmlz(fourth_year_data)
normalized_fifth_year_data = nmlz(fifth_year_data)


# 存储数据
normalized_first_year_data.to_csv("./cleanedData/2017-09-01to2018-09-01stock_price_close.csv")
normalized_second_year_data.to_csv("./cleanedData/2018-09-01to2019-09-01stock_price_close.csv")
normalized_third_year_data.to_csv("./cleanedData/2019-09-01to2020-09-01stock_price_close.csv")
normalized_fourth_year_data.to_csv("./cleanedData/2020-09-01to2021-09-01stock_price_close.csv")
normalized_fifth_year_data.to_csv("./cleanedData/2021-09-01to2022-09-01stock_price_close.csv")

# %%

first_year_cov = first_year_data.cov()
second_year_cov = second_year_data.cov()
third_year_cov = third_year_data.cov()
fourth_year_cov = fourth_year_data.cov()
fifth_year_cov = fifth_year_data.cov()

first_year_cov.to_csv("./cleanedData/2017-09-01to2018-09-01stock_price_close_cov.csv", index=False)
second_year_cov.to_csv("./cleanedData/2018-09-01to2019-09-01stock_price_close_cov.csv", index=False)
third_year_cov.to_csv("./cleanedData/2019-09-01to2020-09-01stock_price_close_cov.csv", index=False)
fourth_year_cov.to_csv("./cleanedData/2020-09-01to2021-09-01stock_price_close_cov.csv", index=False)
fifth_year_cov.to_csv("./cleanedData/2021-09-01to2022-09-01stock_price_close_cov.csv", index=False)

# index=False不要列名，header=False不要行名
# %%
