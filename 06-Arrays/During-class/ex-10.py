arr = [1,2,3,4,5]
arr[0] = arr[0] - 1
arr[-1] = arr[-1]+4
x = int(len(arr)/2)
arr[x]=arr[x]*2
print(arr)