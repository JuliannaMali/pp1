rows = int(input("Enter a number: "))
for i in range(0, rows+1):
    for j in range(0, i+1):
        print("*", end=" ")
    print(" ")

for i in range(rows+1, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print(" ")