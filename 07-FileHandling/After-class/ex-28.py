import re
f = open('txt-ex28.txt', 'r')
file = f.read()
words = re.split('\s', file)

for x in words:
    if ',' in x:
        y = x.replace(',', '')
        z = words.index(x)
        words.pop(z)
        words.insert(z, y)
    if '.' in x:
        y = x.replace('.', '')
        z = words.index(x)
        words.pop(z)
        words.insert(z, y)

for x in words:
    print(x+'\n')

f.close()