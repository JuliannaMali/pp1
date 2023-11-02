def f(amount_to_pay):
    five = 0
    two = 0
    one = 0
    if amount_to_pay>0:
        five += int(amount_to_pay/5)
        temp = amount_to_pay - five*5
        two += int(temp/2)
        one += temp%2
    if amount_to_pay == 0:
        return 0
    return (five + two + one)
if __name__ == '__main__':
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))