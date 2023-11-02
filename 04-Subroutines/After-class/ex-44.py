def f(password):
    if len(password) >= 6:
        password = list(password)
        list1 = []
        for x in password:
            y = password.count(x)
            if y > 1:
                list1.append(0)
            else:
                list1.append(1)
        if 0 in list1:
            return False
        else:
            return True
    else:
        return False
            
if __name__ == '__main__':
    print(f('ax15'))
    print(f('book123'))
    print(f('A2water3'))
    print(f('qwerty'))
    print(f(""))