def f(text):
    list1 = []
    for x in text:
        list1.append(x)
    y = "-".join(list1)
    return y

if __name__ == '__main__':
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))