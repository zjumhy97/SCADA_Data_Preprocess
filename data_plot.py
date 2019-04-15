"""
data_plot.py
作用：将XXX.csv中的数据进行可视化呈现，选取某一列的数据。
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

# 最初的数据先slice出来到test_data_1.csv中，然后到test_data_3.csv中看一下趋势

filename = 'test_data_3.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    temperatures = []
    for row in reader:
        temperature = float(row[19])
        temperatures.append(temperature)

    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(temperatures, c = 'red', alpha = 0.6)
    plt.title('XXX', fontsize = 24)
    plt.xlabel('XXX',fontsize = 16)
    plt.ylabel('XXX', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)  # 这行什么意思
    plt.show()
    
