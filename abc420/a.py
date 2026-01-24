x, y = map(int, input().split())

ret = (x+y)%12
if ret == 0:
	print('12')
else:
	print(ret)

