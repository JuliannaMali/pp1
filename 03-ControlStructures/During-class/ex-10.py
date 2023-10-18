number = str(input("Enter a number "))
if number[0] == "-":
    print(f'|{number} = {number[1:]}')
else:
    print(number)