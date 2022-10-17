import random
n = 1000000
count = 0
def f(x):
    return x*x*x+x*x
for i in range(n):
    x = random.uniform(0, 1)
    y = random.uniform(0, 2)
    if y <= f(x):
        count += 1
i = count/n*2
print(i)