import csv
import json
c = open('products.csv', 'r')
file=csv.reader(c)
j=open('products.json', 'a')
header=[]
rows=[]
header=next(file)
for row in file:
    rows.append(row)

dict1={}
arr=[]
index=0
indexrows=0

while indexrows<len(rows):
    if index==0:
        dict1[f'{header[0]}']=rows[indexrows][0]
    if index==1:
        dict1[header[1]]=int(rows[indexrows][1])
    if index==2:
        dict1[header[2]]=float(rows[indexrows][2])
    index+=1
    if index==3:
        index=0
    if len(dict1)==3:
        arr.append(dict1.copy())
        dict1.clear()
        indexrows+=1

json.dump(arr, j, indent=6)
c.close()
j.close()