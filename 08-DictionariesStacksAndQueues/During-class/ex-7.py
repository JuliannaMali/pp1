person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#a
print(person)
#b
print(person["name"])
#c
print(person["hobby"])
#d
person["surname"] = 'Nowak'
#e
person['married']= not person['married']
#f
person.update({'gender':'male'})
#g
person['hobby']+=['bicycle']
#h
person['phone'].update({'work':'313131444'})
print(person)