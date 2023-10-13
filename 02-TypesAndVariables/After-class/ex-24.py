registration = str(input("Enter regitration number: "))
x = (registration[0:2] == "KR") or (registration[0:2] == "KK")
print(f'Car from Kraków: {x}')
