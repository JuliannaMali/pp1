def f(uid):
    list1 = []
    for i in uid:
        list1.append(uid.count(i))
    for i in list1:
        if i!=1:
            return False
        else:
            pass
    return True
    
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2","bob2"]))
print(f(["bob2","BOB2"]))
