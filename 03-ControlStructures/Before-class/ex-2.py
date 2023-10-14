hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    if hours > 40:
        extra = hours - 40
        pay = 40*rate + extra*(1.5*rate)
        print(f'Pay: {pay}')
    else:
        pay = rate*hours
        print(f'Pay: {pay}')
except:
    print("Error, please enter numeric input")