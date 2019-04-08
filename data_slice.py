"""
data_slice.py
作用：将XXX.csv中的第n行到第m行的数据剪切至YYY.csv中，作为数据中转。
"""

import csv

# 这里注意一下，写入文件时，要加newline=‘’才会在最终的csv文件中没有间隔行
filetoread=open('changtu1_5min_1.csv','r')
filetowrite=open('test_data_2.csv','w',newline='')
reader=csv.reader(filetoread)
writer=csv.writer(filetowrite)

# 0<=n<=m
n=0
m=1000

# i为循环次数
i=0

for row in reader:
    if i<n or i>m:
        pass   
    else:
        writer.writerow(row)
    i=i+1

filetoread.close
filetowrite.close
