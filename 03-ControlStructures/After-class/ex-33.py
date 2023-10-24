x = int(input("Enter a decimal number: "))
temp = x
list = []
while x > 0:
    y = x % 2
    list.insert(0, str(y))
    x = int(x/2)
    
binary = ''.join(list)
print(f'{temp}(10) = {binary}(2)')
print(bin(temp))