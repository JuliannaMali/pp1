list = [0, 1]
while len(list) <= 19:
    z = list[len(list) - 1] + list[(len(list))-2]
    list.append(z)
print(list)