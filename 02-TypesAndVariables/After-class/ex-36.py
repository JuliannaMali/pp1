buys = round(float(input("For how much does the bank buy EUR? ")), 4)
sells = round(float(input("For how much does the bank sell EUR? ")), 4)

spread = round(sells-buys, 4)
print(f'The spread is {spread}')
