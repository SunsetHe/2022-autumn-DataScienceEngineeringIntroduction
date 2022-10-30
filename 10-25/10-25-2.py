import matplotlib.pyplot as plt
import csv

import numpy as np

f = open('daily_KP_SUN_2020.csv','r',encoding='gb18030',errors='ignore')
f1 = csv.reader(f)
the_file = list(f1)
f.close()

pure_data = []

for i in range(9):
    pure_data.append([])

for i in range(3,277):
    month = int(the_file[i][1])
    value = float(the_file[i][3])
    pure_data[month - 1].append(value)

#现在pure_data这一二维列表的第一个参数表示月份（+1）第二个参数表示日（+1）

shining_time_sum = []
for i in range(9):
    shining_time_sum.append(0)

for month in range(9):
    for value in pure_data[month]:
        shining_time_sum[month] += value
    print(shining_time_sum[month])

shining_time_average = []
for i in range(9):
    shining_time_average.append(0)

for month in range(9):
    shining_time_average[month] = shining_time_sum[month]/len(pure_data[month])
    print(shining_time_average[month])

x1 = np.arange(1,10)
y1 = np.array(shining_time_sum)
plt.subplot(121)
plt.bar(x1,y1)

x2 = np.arange(1,10)
y2 = np.array(shining_time_average)
plt.subplot(122)
plt.bar(x2,y2)

plt.show()