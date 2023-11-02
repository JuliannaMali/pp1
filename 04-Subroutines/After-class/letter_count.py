def letter_calculation(text, letter):
    x = text.count(letter)
    return x
if __name__ == '__main__':
    print(letter_calculation("You never get a second chance to make a first impression", "e"))