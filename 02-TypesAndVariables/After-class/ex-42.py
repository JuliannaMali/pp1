binary_number = input("Input a 4 digit binary number")
list1 = []
list2 = []
suma = []

if len(binary_number) > 4:
    print("You have to input a four digit binary number")
else:
    list1 = (list(binary_number))
    print(list1)
    for i in range(len(list1)):
        list2.append(int(list1[i]))

print(list2)

if list2[0] == 1:
    suma.append(8)
else:
    suma.append(0)

if list2[1] == 1:
    suma.append(4)
else:
    suma.append(0)

if list2[2] == 1:
    suma.append(2)
else:
    suma.append(0)

if list2[3] == 1:
    suma.append(1)
else:
    suma.append(0)

print(suma)                          
print(sum(suma))



            