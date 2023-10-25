def read_number():
    x = int(input("Enter a number: "))
    return x
if __name__ == "__main__":
    x = read_number()
    y = read_number()
    z = x + y
    print(f'{x} + {y} = {z}')