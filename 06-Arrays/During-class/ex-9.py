arr=[2,3,7,5,4]
#a
print(f'(Array: {arr}')
#b
print(f'No ofelements: {len(arr)}')
#c
print(f'First value: {arr[0]}')
#d
print(f'Second value: {arr[1]}')
#e
print(f'Last value: {arr[-1]}')
#f
x = len(arr) -2
print(f'Last but one vaue {arr[x]}')
#g
first = arr[0]
last = arr[-1]
sum = first + last
print(f'Sum of the first and last is: {sum}')
#h
y = int((len(arr))/2)
print(f'Middle value is: {arr[y]}')
#i
for x in arr:
    print(x, end=" ")