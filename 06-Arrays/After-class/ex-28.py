def compare(array1, array2):
    if len(array1)==len(array2):
        yes=[]
        for x in range(0, len(array1)):
            if array1[x] == array2[x]:
                yes.append(0)
            else:
                yes.append(1)
        if 1 in yes:
            return False
        else:
            return True
    else:
        return False
    
#a
arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]
if compare(arr1, arr2) == True:
    print(f'Array1: {arr1}\nArray2: {arr2}\nComparison:arrays are the same')
else:
    print(f'Array1: {arr1}\nArray2: {arr2}\nComparison:arrays are different')

#b
arr3 = [True, False]
arr4 = [True, False, True]
if compare(arr3, arr4) == True:
    print(f'Array1: {arr3}\nArray2: {arr4}\nComparison:arrays are the same')
else:
    print(f'Array1: {arr3}\nArray2: {arr4}\nComparison:arrays are different')

#c
arr5 = [5,3,1]
arr6 = [5,3,1]
if compare(arr5, arr6) == True:
    print(f'Array1: {arr5}\nArray2: {arr6}\nComparison:arrays are the same')
else:
    print(f'Array1: {arr5}\nArray2: {arr6}\nComparison:arrays are different')

#d
arr7 = [3,2,1]
arr8 = [3,2]
if compare(arr7, arr8) == True:
    print(f'Array1: {arr7}\nArray2: {arr8}\nComparison:arrays are the same')
else:
    print(f'Array1: {arr7}\nArray2: {arr8}\nComparison:arrays are different')