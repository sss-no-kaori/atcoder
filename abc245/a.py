n = int(input())

ret = 0
for i in range(1, n+1):
    ret = ret + ((-1)**i)*(i**3)
print(ret)
