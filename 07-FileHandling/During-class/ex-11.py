file = open("numbers.txt", "r")
numbers =[]
display = []
for line in file:
    numbers.append(int(line))

for x in numbers:
    display.append(str(x))

z = " ".join(display)
print(f'Numbers: {z}')
suma = sum(numbers)
print(f'Sum: {suma}')

file.close()