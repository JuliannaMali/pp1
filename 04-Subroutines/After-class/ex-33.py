def f(n):
    list1=[]
    for i in range(1, n+1):
        list1.append("*")
    return "/".join(list1)
if __name__ == '__main__':
    print(f(4))
    print(f(1))