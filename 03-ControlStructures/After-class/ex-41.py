code = "0805"
code_enter = str(input("Enter the PIN code: "))
tries = 0
while tries <= 2:
    if code_enter == code:
        print("Correct")
        break
    else:
        tries += 1
        if tries == 3:
            break
        else:    
            print("Incorrect")
            code_enter = str(input("Enter the PIN code"))
if tries > 2:
    print("Sorry, your payment card has been blocked")
    