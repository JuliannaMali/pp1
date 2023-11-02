import random
def generate_number():
    x = random.randint(1, 10)
    return x
if __name__ == '__main__':
    print(generate_number())