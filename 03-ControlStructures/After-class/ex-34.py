amount = int(input("Enter the amount in PLN: "))
five = 0
two = 0
one = 0
if amount > 0:
    five += int(amount/5)
    temp = amount - five*5
    two += int(temp/2)
    one += temp%2
print(f'5zł - {five} \n2zł - {two} \n1zł - {one}')
