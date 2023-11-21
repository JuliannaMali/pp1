arr=[15, 8, 31, 47, 2, 19]
sum = 0
i=0
while i in range(0, len(arr)):
    sum+=arr[i]
    i+=1
print(f'Array: {arr}')
print(f'Arithmetic mean of this array: {sum/len(arr)}')