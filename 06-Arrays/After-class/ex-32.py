def occurs(number,array):
    if number in array:
        return True
    else: return False

arr=[15, 38, 7, 23, 14]
x = int(input("Number:"))
def occurs2(nr, array):
    if nr in array:
        return True
    else: return False
occurs2(x, arr)
print(f'Array is {arr}')

if occurs(x,arr) == True:
    print(f'Result: number {x} appears in the array')