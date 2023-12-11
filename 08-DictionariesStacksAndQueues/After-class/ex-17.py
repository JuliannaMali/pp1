dict1={
    'A':'Alfa',
    'B':'Bravo',
    'C':'Charlie',
    'D':'Delta',
    'E':'Echo',
    'F':'Foxtrot',
    'G':'Golf',
    'H':'Hotel',
    'I':'India',
    'J':'Juliett',
    'K':'Kilo',
    'L':'Lima',
    'M':'Mike',
    'N':'November',
    'O':'Oscar',
    'P':'Papa',
    'Q':'Quebec',
    'R':'Romeo',
    'S':'Sierra',
    'T':'Tango',
    'U':'Uniform',
    'V':'Victor',
    'W':'Whiskey',
    'X':'Xray',
    'Y':'Yankee',
    'Z':'Zulu',
}

text=str(input("Enter text: "))
txt=text.upper()
translate=[]
for x in txt:
    for key,value in dict1.items():
        if x == key:
            translate.append(value)
print(f'Spelled text: {" ".join(translate)}')