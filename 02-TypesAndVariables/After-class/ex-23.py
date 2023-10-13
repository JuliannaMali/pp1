import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
circumference = a + b + c
print(f'Triangle circumference: {circumference}')
s = circumference/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'Triangle area: {area}')