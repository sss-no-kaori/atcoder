a, b, c = map(int, input().split())

data = sorted([a, b, c])
print(data[2]*100+data[1]*10+data[0])

