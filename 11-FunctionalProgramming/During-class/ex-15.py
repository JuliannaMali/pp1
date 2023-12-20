text= str(input('Text: '))

ln = list(map(lambda x: len(x), text.split()))

print(f'No, of letters in words: {ln}')