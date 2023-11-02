def f(number):
    strnumber = str(number)
    list1 = []
    suma = []
    for x in strnumber:
        list1.append(int(x))
    for x in list1:
        y = list1.count(x)
        if y > 1:
            suma.append(x)
    if len(suma) == 0:
        return 0
    else:
        return sum(suma)

if __name__ == '__main__':
    print(f(1027))
    print(f(230335))
    print(f(513553007))