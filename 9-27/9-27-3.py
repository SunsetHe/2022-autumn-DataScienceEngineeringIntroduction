s = input()
countlist = [1 for i in range(len(s))]

for i in range(len(s)):
    j = i + 1
    while j < len(s) and s[i] == s[j] :
        countlist[i] += 1
        j += 1

if max(countlist) == 1:
    print('no')
else:
    print(max(countlist))
