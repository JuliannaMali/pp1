def different(n1,n2,n3):
    if n1 != n2  and n2 != n3 and n3!= n1:
        return True
    else:
        return False
x = input("Enter the first number: ")
y = input("Enter second number: ")
z = input("Enter third number:")
if different(x,y,z) == True:
    print(f"Numbers {x}, {y}, {z} are different")