name1 = input("Enter first peron name: ")
age1 = int(input("Enter first person age: "))
name2 = input("Enter second person name: ")
age2  = int(input("Enter second peron age:: "))

if age1 >= 18 and age2>=18:
    print(f'Both {name1} and {name2} are adults')
else:
    print('At least one of them is not an adult')
