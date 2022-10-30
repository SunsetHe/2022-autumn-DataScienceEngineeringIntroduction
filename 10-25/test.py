"""import csv
f = open('daily_KP_SUN_2020.csv','r',encoding='gb18030',errors='ignore')
f1 = csv.reader(f)
thefile = list(f1)
for i in thefile:
    print(i)
f.close()

#import numpy as np  # 通常习惯以np代指NumPy，后续调用时无需再输入过多前缀
#arr1 = np.empty((4,3),dtype=float)  # 创建一个4行3列，元素类型是浮点类型的二维数组，各元素值未知
#print(arr1)

#import matplotlib.pyplot as plt
#import numpy as np
#import math
#
#x = np.arange(0, 4*math.pi,0.1)
#y = np.sin(x)
#
#plt.plot(x,y)
#plt.show()
#a = []
#a.append([])
#a[0].append(2.0)
#print(a[0][0])"""

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0,4*math.pi,0.1)
y1 = np.sin(x)
y2 = np.sin(2*x)

plt.plot(x,y1,label='y=sin(x)')
plt.plot(x,y2,label='y=sin(2x)')
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()