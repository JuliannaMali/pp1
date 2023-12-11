import json
f = open('students.json', 'r')
file = json.load(f)
l=open('limited.json', 'a')
arr=[]
for x in file:
    dict1={}
    for key,value in x.items():
        if key=='name' or key=='surname' or key=='student_ID':
            dict1.update({key:value})
    arr.append(dict1.copy())

json.dump(arr,l, indent=6)


f.close()
l.close()