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
f = open("ICAO.txt", 'a')
for key,value in dict1.items():
    f.write(f"{key} {value}"+'\n')
f.close()