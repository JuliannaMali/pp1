def numbers(n):
    list1 = []
    for i in range(1, n+1):
        list1.append(str(i))
    string = " ".join(list1)
    return(string)
n_input = int(input("Enter n: "))
print(f"Numbers <1, {n_input}>: {numbers(n_input)}")