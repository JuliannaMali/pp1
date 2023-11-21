def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return

arr1=[1,2,3,4,5,6]
arr2=[3,2,1,5,4,7]
arr3=[7,9,10,21,1]

bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)


for i in range(len(arr1)):
    print("% d" % arr1[i], end=" ")
    
for i in range(len(arr2)):
    print("% d" % arr2[i], end=" ")

for i in range(len(arr3)):
    print("% d" % arr3[i], end=" ")