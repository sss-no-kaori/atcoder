s, a, b, x = map(int, input().split())

d = x // (a + b)
m = x % (a + b)
if m > a:
    m = a
print((s*a*d)+(s*m))
