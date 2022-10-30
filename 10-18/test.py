"""import time

scale = 50
print("start".center(scale//2,'-'))
start = time.perf_counter()

for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print('\n'+"end".center(scale//2,'-'))
f1 = open(r'D:\desktop\test.txt','r')
s = f1.readlines()
print(s)
for i in range(5):
    line = f1.readline()
    print(line,end='')
f1.seek(0)
s = f1.readline()
print(s,end='') 
weather = {'北京':27.2, '天津':26.5, '上海':28.2, '重庆':30.1}
f2 = open(r'D:\desktop\test.txt','w')
for key,value in weather.items():
    s = key + ' ' + str(value) + '\n'
    f2.write(s)
f3 = open(r'D:\desktop\test2.txt','w')
song = {'someone like you':'adele','cherry blossom':'lana del rey','one last kiss':'宇多田光'}
for key,value in song.items():
    s = value + " 's " + key + '\n'
    f3.write(s)
f3.close()"""

import csv

f1 = open("stuGrade.csv","r")
thefile = csv.reader(f1)
Thefile = list(thefile)
print(Thefile)
print(Thefile[0][0])
for i in Thefile:
    print(i)
print(list.__len__(Thefile))