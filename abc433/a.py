x, y, z = map(int, input().split())

ret = False
loop_max = 100 - max(x, y) + 1
for i in range(0, x + 1):
	x_age = x + i
	y_age = y + i
	if x_age == y_age * z:
		ret = True
		break

if ret:
	print('Yes')
else:
	print('No')

