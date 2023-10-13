name = input()
list1 = list(name)
list2 = []
for i in range(len(list1)):
    x = ord(list1[i])
    list2.append(x)

print(list2)