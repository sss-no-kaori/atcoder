n = int(input())
a_list = map(int, input().split())

is_odd = True
ret = 0
for a in a_list:
    if is_odd:
        ret = ret + a
        is_odd = False
    else:
        is_odd = True
print(ret)
