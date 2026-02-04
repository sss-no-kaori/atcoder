s = input()

ret = ''
for i in range(len(s)):
    if ord(s[i]) < 97:
        ret = ret + s[i]
print(ret)
