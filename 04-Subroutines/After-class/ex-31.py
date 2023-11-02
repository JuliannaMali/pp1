def f(x,y):
    list1 = []
    if x <0 and y>0:
        for i in range(x, 0):
            if i%2 == 0:
                list1.append(i)
    return len(list1)

if __name__ == '__main__':
    print(f(-7, 8))
    print(f(-1, 11))