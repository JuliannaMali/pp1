entry_price = float(input("Enter the price "))
discount = float(input("Enter the discout (in %) "))

reduction = round(entry_price * (discount/100), 2)
discount_price = round(entry_price - reduction, 2)

print(f'Entry price was {entry_price}')
print(f'Discount was {discount}')
print(f'Price with discount is {discount_price}')
print(f'Reduction is {reduction}')