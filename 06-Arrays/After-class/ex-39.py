arr = [1,2,3,4,5,6,7,8,9,10]
even =[]
odd=[]
for x in arr:
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)

even.extend(odd)
print(even)