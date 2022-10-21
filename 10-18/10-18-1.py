f1 = open(r'D:\desktop\test.txt','r')
s = f1.readline()
print(s)

f1.seek(0)

s2 = f1.readlines()
print(s2)