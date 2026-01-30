s = input()

a2z_set = set()
for i in range(ord('a'), ord('z')+1):
    a2z_set.add(chr(i))

for i in range(len(s)):
    w = s[i]
    if w in a2z_set:
        a2z_set.remove(w)

print(a2z_set.pop())
