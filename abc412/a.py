n = int(input())
ab_list = []
for i in range(n):
    ab_list.append(map(int, input().split()))

ret = 0
for a, b in ab_list:
    if a < b:
        ret = ret + 1

print(ret)
