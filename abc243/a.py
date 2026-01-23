x, c = map(int, input().split())

loop_max = (x // 1000)

kin = 0
for i in range(loop_max, 0, -1):
    tesuryo = i * c
    if (i * 1000 + tesuryo) <= x:
        kin = i * 1000
        break

print(kin)
