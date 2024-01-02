def f(x,y,digit):
    suma = 0
    for i in range(x, y+1):
        i = str(i)
        digit = str(digit)
        if digit in i:
            x = i.count(digit)
            suma+=x
    return suma

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))