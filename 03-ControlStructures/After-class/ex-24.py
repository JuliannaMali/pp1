current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))
reduce = 0

if current_price < previous_price:
    reduce = 100 - (current_price/previous_price*100)
    print(f'''Buy the product!!
Product price reduced by {reduce}%''')