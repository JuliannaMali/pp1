import if_in_range
x = int(input("Enter a number: "))
y = int(input("Range from: "))
z = int(input("Range to: "))
if if_in_range.if_in_range(x, y, z) == True:
    print(f'Number {x} in the range <{y}, {z}>: yes')
else:
    print(f'Number {x} in the range <{y}, {z}>: no')