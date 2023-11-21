arr1=[]
arr2=[]
subset=[]
for x in arr1:
    if x in arr2:
        subset.append(0)
    else:
        subset.append(1)
if 1 in subset:
    print("Array 1 is not a subset of array2")
else:
    print("Array1 is a subset of array2")