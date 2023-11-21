arr=[2, 3, 2, 5, 8, 1, 9, 8]
unique=[]
for x in arr:
    y=arr.count(x)
    if y == 1:
        unique.append(str(x))
print(f'Unique numbers in array are: {" ".join(unique)}')