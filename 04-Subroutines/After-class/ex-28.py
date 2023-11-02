def f(binary_number):
    x = str(binary_number)
    list1 = []
    for n in range(0, len(x)):
        if x[n] == "0" or x[n] == "1":
            list1.append(x[n])
        else:
            pass
    if len(list1) == len(x):
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f(101101))
    x = "111a11"
    print(f(x))