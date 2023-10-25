def phone_keyboard():
 for i in range(1, 10):
    if i  %3 == 0:
        print(f'{i}')
    else:
        print(f"{i}", end=" ")
    
print(phone_keyboard())