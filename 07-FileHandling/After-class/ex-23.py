f = open('txt-ex23.txt', 'a')

for x in range(1, 11):
    y = x**2
    z = x**3
    f.write(f'{x}, {y}, {z}' + '\n')