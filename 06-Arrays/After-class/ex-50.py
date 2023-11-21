arr = [[-38, 19], [5,40],[-7,11],[29,16]] 
list1 = []
for i in arr:
    for j in i:
        list1.append(j)
x = min(list1)
y = max(list1)

for i in arr:
    for j in i:
        if j == x:
            a = arr.index(i)
            z = i.index(j)
            print(f'Index of minimum: [{a}][{z}]')
        if j == y:
            a = arr.index(i)
            z = i.index(j)
            print(f'Index of maximum: [{a}][{z}]')