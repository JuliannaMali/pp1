def f(n):
    list1 = []
    i = 1
    for i in range(1, n+1):
        list1.append(str(i))
        i += 1
    return("".join(list1))

if __name__ == '__main__':
    print(f(11))
    print(f(4))