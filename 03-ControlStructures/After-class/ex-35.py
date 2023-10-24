i = 1
list = []
while i <=30:
    if i%3 == 0 and i%5 == 0:
        list.append("BINGO")
    elif i%3 == 0 and i%5 != 0:
        list.append("THREE")
    elif i%3 != 0 and i%5 == 0:
        list.append("FIVE")
    else:
        list.append(str(i))
    i += 1
print(" ".join(list))