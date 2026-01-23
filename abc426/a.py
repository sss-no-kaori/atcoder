x, y = input().split()

os = ['Ocelot', 'Serval', 'Lynx']

x_index = os.index(x)
y_index = os.index(y)

if x_index >= y_index:
    print('Yes')
else:
    print('No')
