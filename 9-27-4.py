s = input()
new = list(s)
for i in range(new.count(' ')):
    new.remove(' ')
for i in range(len(new)):
    print(new[i],end='')
