hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours > 40:
    extra = hours - 40
    pay = 40*rate + extra*(1.5*rate)
    print(f'Pay: {pay}')
else:
    pay = rate*hours
    print(f'Pay: {pay}')
