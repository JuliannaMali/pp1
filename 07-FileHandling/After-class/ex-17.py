f = open('txt-ex17.txt', 'r', encoding='UTF-8')
list1 = []
for line in f:
    list1.append(line)

counter = 0
while counter in range(0, len(list1)):
    if counter == 0:
        print(list1[0])
        counter +=1
    elif counter != 0 and counter%5 !=0:
        print(list1[counter])
        counter+=1
    else:
        x = input("Press Enter")
        while x == "":
            print(list1[counter])
            counter +=1
            if counter%5==0:
                break

f.close()