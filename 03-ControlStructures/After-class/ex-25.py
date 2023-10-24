number_of_products = int(input("Number of products purchased: "))
price = int(input("Product price: "))
pay = 0

if number_of_products > 2:
    pay += (number_of_products - 2)*(price*0.75)+2*price
else:
    pay+= number_of_products*price

print(f'Amunt to pay: {pay}')