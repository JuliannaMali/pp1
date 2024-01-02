# 1, 2, 3, 4, 5, 6, 7
# a - d
# A - D
# +, - na początku

def f(mnumbers):

    suma = 0

    for number in mnumbers:
        temp = 0
        if number[0]=="+" or number[0]=='-':
            number = number.replace(number[0], "")
        if ("+" in number) or ("-" in number):
            temp += 1
        for i in number:
            if 'e' <= i <= 'z' or 'E' <= i <= 'Z':
                temp += 1
            else:
                for x in range(8, 10):
                    try:
                        if int(i) == x or int(i) == 0:
                            temp += 1
                    except ValueError:
                        pass
                
        if temp == 0:
            suma += 1
        
    return suma 

print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))