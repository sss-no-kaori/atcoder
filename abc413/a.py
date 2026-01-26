n, m = map(int, input().split())
a_list = map(int, input().split())

if sum(a_list) <= m:
    print('Yes')
else:
    print('No')
