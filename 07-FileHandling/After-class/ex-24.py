import csv
f = open('txt-ex24.csv', 'r')
file = csv.reader(f)
header=[]
rows=[]
header=next(file)
for row in file:
    rows.append(row)

for row in rows:
    if int(row[2])<30:
        print(f'{row[0]}    {row[1]}    {row[-1]}')

f.close()