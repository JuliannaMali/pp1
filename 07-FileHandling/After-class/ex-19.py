f = open('txt-ex19.txt', 'r', encoding='UTF-8')
copy = open('copylines.txt', 'a')

for line in f:
    copy.write(line)

f.close()
copy.close()