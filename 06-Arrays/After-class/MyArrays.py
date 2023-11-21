arr=[7,3,8,5,2]
#a
def second_largest(arr):
    x = max(arr)
    y=1
    snd_lrg =[]
    while len(snd_lrg) == 0:
        if x-y in arr:
            snd_lrg.append(x-1)
        else:
            y-=1
    return snd_lrg

def differnce(arr):
    x = max(arr)
    y=min(arr)
    return x-y

def median(arr):
    if len(arr)%2!=0:
        return arr[len(arr)//2]
    else:
        x = arr[len(arr)//2]
        y = arr[len(arr)//2-1]
        median = (x+y)/2
        return median

def arr_min_max(arr):
    x = min(arr)
    y = max(arr)
    list1=[x, y]
    return list1
def string(arr):
    temp =[]
    for x in arr:
        temp.append(str(x))
    return "-".join(temp)

print(f'Numbers: {arr}')
print(f'Second largest number: {second_largest(arr)}')
print(f'Median: {median(arr)}')
print(f'Smallest and largest number: {arr_min_max(arr)}')
print(f'Numbers as a string: {string(arr)}')