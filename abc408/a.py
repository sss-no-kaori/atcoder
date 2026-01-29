n, s = map(int, input().split())
t_list = list(map(int, input().split()))

t_list.insert(0, 0)

ret = False
for i in range(1, n+1):
    interval = t_list[i] - t_list[i-1]
    if interval > s:
        ret = True
        break

if ret:
    print('No')
else:
    print('Yes')
