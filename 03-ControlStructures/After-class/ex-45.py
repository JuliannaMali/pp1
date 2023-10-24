list = []
n = int(input("Enter N: "))
i = 1
while len(list) <= n:
    if len(list) == n:
        break
    else:
        dividers = []
        d = 1
        while d < (i+1):
            if i%d == 0:
                dividers.append(d)
            d += 1
        if len(dividers) == 2:
            list.append(i)
        i += 1
print(list)