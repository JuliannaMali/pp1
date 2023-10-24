list = []
if len(list) == 0:
    list.append("temp")
    while list[len(list) - 1] != 0:
        number = int(input("Enter number: "))
        list.append(number)
        if "temp" in list:
            list.remove("temp")
        if list[(len(list) - 1)] == 0:
            break

quantity = (len(list) - 1)
suma = sum(list)
mean = suma/quantity
print(f'RESULT:\nQuantity: {quantity}\nSum: {suma}\nMean: {mean}')