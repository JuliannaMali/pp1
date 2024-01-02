def f(vname):
    if 1 <= len(vname) <= 5 and ("a" <= vname[0] <= "z" or "A" <= vname[0] <= "Z" or vname[0] == "_"):
        return True
    else:
        return False
    
print(f("abc"))
print(f("Abc"))
print(f("aBC"))
print(f("_ab_c"))
print(f("abdcef"))
print(f("8abc"))
print(f("_aB8_"))
print(f("_4x"))