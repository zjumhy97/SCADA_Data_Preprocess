"""
data_paste.py
作用：将XXX.csv中的第n行到第m行的数据剪切粘贴至YYY.csv中，用于合并数据。
"""

import csv

filetoread=open('test_data_3.csv','r')  # 处理好的一小部分数据
filetowrite=open('test_data_5.csv','a',newline='')  # 粘贴到test_data_5.csv中
reader=csv.reader(filetoread)
writer=csv.writer(filetowrite)

# 0<=n<=m
n=1
m=120

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
