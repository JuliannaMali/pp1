name = str(input("Enter name: "))
lenght = len(name)
if name[lenght-1] == "a":
    print(f'{name} - Polish female name')
else:
    print(f'{name} - not a Polish female name')