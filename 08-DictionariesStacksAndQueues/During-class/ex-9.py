countries = [
    {"name":"Poland", "population":38000000},
    {'name':'Norway', 'population':5408000},
    {'name':'Germany',"population":83200000},
    {'name':'Sweden',"population":10420000},
    {'name':'Austria',"population":9000000}
]

print('{:<10}{:<15}'.format('COUNTRY', 'POPULATION'))
index=0
while index<len(countries):
    country=countries[index]
    print('{:<10}{:<15}'.format(country['name'], country['population']))
    index+=1