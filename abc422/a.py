s = input()

world = int(s[0])
stage = int(s[2])

if stage == 8:
	world = world + 1
	stage = 1
else:
	stage = stage + 1

print(f'{world}-{stage}')

