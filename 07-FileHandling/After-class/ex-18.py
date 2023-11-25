f = open('txt-ex18.txt', "r", encoding='UTF-8')
c = open('copy.txt', 'a')

file = f.read()
c.write(file)

f.close()
c.close()