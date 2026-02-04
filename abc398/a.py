n = int(input())

h = n // 2
if n % 2 == 0:
    print('-'*(h-1) + '==' + '-'*(h-1))
else:
    print('-'*(h) + '=' + '-'*(h))
