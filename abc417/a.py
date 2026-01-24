n, a, b = map(int, input().split())
s = input()

s_index = a
f_index = len(s) - b
print(s[s_index:f_index])

