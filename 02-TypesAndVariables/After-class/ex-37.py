data = "Mr. John May, born on 1998-02-16"
name = data[4:8]
surname = data[9:12]
initials = data[4]
initials2 = data[9]
born = data[22:]
print(f'Description: {data}')
print(f'Name: {name}')
print(f'Surname : {surname}')
print(f'Initials: {initials}{initials2}')
print(f'Born: {born}')