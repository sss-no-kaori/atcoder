n = int(input())
t = input()
a = input()

ret = 0
for i in range(n):
    if t[i] == 'o' and a[i] == 'o':
        ret = ret + 1
if ret == 0:
    print('No')
else:
    print('Yes')
