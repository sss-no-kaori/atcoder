n = int(input())
a_list = map(int, input().split())
k = int(input())

ret = 0
for a in a_list:
    if k <= a:
        ret = ret + 1
print(ret)
