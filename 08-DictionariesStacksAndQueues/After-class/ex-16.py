Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

hinkrk=[]
hinsop=[]
avgkrk=[]
avgsop=[]
for x in Hotels_in_Krakow:
    for key,value in x.items():
        if key=='name':
            hinkrk.append(value)
        if key=='price':
            avgkrk.append(value)
for x in hotels_in_Sopot:
    for key,value in x.items():
        if key=='name':
            hinsop.append(value)
        if key=='price':
            avgsop.append(value)
x = sum(avgkrk)/len(avgkrk)
y= sum(avgsop)/len(avgsop)

print(f'Hotels in Kraków: {','.join(hinkrk)}')
print(f'Average hotel price in Kraków: {x}')
print(f'Hotels in Sopot: {','.join(hinsop)}')
print(f'Average hotel price in Sopot: {y}')
if x>y:
    print("Cheaper hotels in: Sopot")
else:
    print("Cheaper hotels in: Kraków")