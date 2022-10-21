f1 = open(r'D:\desktop\stuGrade.csv','r')
Grade = {'Chinese' : 0, 'Math' : 0, 'English' : 0}

f1.readline()

for i in range(5):
    f1.read(6)
    Grade['Chinese'] += float(f1.read(2))
    f1.read(1)
    Grade['Math'] += float(f1.read(2))
    f1.read(1)
    Grade['English'] += float(f1.read(2))
    f1.read(1)

f1.close()

Grade['Chinese'] /= 5
Grade['Math'] /= 5
Grade['English'] /= 5

"""
作业2为以上部分
"""

f2 = open('D:\desktop\my.txt','w')
'''这里我自己选择在本地的桌面上创建的这个my.txt'''

s = '10215501442-黄梓豪,{:.2f},{:.2f},{:.2f}\n'.format(Grade['Chinese'],Grade['Math'],Grade['English'])
f2.write(s)

import time

t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f2.write(t)

s = '\n'
f2.write(s)

time.sleep(2)

t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f2.write(t)