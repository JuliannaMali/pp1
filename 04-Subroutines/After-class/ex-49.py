def f(dice):
    list1 = []
    for x in dice:
        y = int(x)
        list1.append(y)
    list2 = []
    for x in list1:
        y = list1.count(x)
        list2.append(y)
    x = list2.index(max(list2))
    return(list1[x])

if __name__ == '__main__':
    print(f("5233165554211"))
    print(f("2133"))
    