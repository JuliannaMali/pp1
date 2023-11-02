def f(card_number):
    x = str(card_number)
    list1 = []
    for n in range(0, len(x)):
        list1.append((x[n]))
        n += 1
    for i in range(2,12):
        list1[i] = "*"
        i += 1
    y = "".join(list1)
    return y    
    
if __name__ == '__main__':
    print(f(1111111111111111))
