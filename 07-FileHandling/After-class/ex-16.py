def func(file):
    with open(file) as f:
        counter = 0
        for line in f:
            if line != "":
                counter += 1
            else:
                break
        return counter
    
x = str(input("Enter file name: "))
print(func(x))