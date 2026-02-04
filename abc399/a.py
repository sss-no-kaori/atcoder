n = int(input())
s = input()
t = input()

ret = 0
for i in range(n):
    if s[i] != t[i]:
        ret = ret + 1
print(ret)
