import letter_count
x = str(input("Sentence: "))
y = str(input("Letter to be calculated: "))
print(f'The number of letter "{y}": {letter_count.letter_calculation(x, y)}')