def f(product_code):
    list1 = [int(product_code[0]), int(product_code[1]), int(product_code[2])]
    y = sum(list1)
    if int(product_code[3]) == y%7:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f("1082"))
    print(f("2035"))
    print(f('1114'))
    print(f('7071'))
    