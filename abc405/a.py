r, x = map(int, input().split())

rate_min = {
    1: 1600,
    2: 1200
}
rate_max = {
    1: 2999,
    2: 2399
}

if rate_min[x] <= r and r <= rate_max[x]:
    print('Yes')
else:
    print('No')
