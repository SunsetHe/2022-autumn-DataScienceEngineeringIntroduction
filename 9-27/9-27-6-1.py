n = 2
near = 0

while near**2 < n:
    if (near + 1)**2 > n:
        break
    else:
        near += 1

while n - (near**2) > 0.0001 :
    near += 0.00001

print(near)