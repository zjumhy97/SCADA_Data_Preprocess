"""
data_fill.py
作用：将XXX.csv中的缺失数据补齐。
"""

import csv
import numpy as np
import pandas as pd

scada_data = pd.read_csv('test_data_1.csv',encoding='gbk')

# filetowrite=open('test_data_3.csv','w',newline='')
# writer=csv.writer(filetowrite)
# print(scada_data.sample(5))

# 检查每列有多少数据值是空白的
# missing_values_count = scada_data.isnull().sum()
# print(missing_values_count[0:10])

# 检查数据的缺失率
# total_cells =  np.product(scada_data.shape)
# total_missing = missing_values_count.sum()
# print(total_cells)
# print(total_missing)
# print(total_missing / total_cells * 100)

# 填充缺失值，如果都是NaN填充为0
scada_data.fillna(0).to_csv('test_data_3.csv',encoding='gbk',index = False)

# 填充缺失值，将NaN填充为该列下一行的值
# 这个对我没有多大用，但是可以参考，应该有填充为上一行的值
# scada_data.fillna(method = 'bfill', axis = 0).fillna("0")
# method = 'ffill', axis = 0 index; axis = 1, columns

# scada_data.fillna(method = 'ffill', axis = 0).to_csv('test_data_3.csv',encoding='gbk')

