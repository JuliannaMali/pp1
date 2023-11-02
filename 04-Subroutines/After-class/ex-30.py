def f(number,even):
    list1 = []
    even_number = []
    odd = []
    temp = str(number)
    for x in range(len(temp)):
        y = temp[x]
        list1.append(int(y))  
    i = 0
    for i in range(0, len(list1)):
        if list1[i]%2 == 0:
            temp1 = list1[i]
            even_number.append(int(temp1))
        else:
            temp2 = list1[i]
            odd.append(int(temp2))
        i += 1
    if even == True:
        return sum(even_number)
    else:
        return sum(odd)
    
if __name__ == '__main__':
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))