n, l, r = map(int, input().split())
xy_list = []
for i in range(n):
    xy_list.append(map(int, input().split()))

ret = 0
for x, y in xy_list:
    if x <= l and r <= y:
        ret = ret + 1

print(ret)
