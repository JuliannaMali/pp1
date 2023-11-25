import re
msg = 'To be, or not to be, that is the question'
words = re.split('\s', msg)
for x in words:
    if ',' in x:
        y = x.replace(',', '')
        z = words.index(x)
        words.pop(z)
        words.insert(z, y)
print(words)