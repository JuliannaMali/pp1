import re
f = open('txt-ex29.txt', 'r')
file = f.read()
grades=re.findall('\d''.''\d'',', file)
grades2=[]
for x in grades:
    if ',' in x:
        y = x.replace(',', '')
        z = grades.index(x)
        grades.pop(z)
        grades.insert(z, y)
for x in grades:
    y = float(x)
    grades2.append(y)

x = round(sum(grades2)/len(grades2), 2)

print(x)
f.close()