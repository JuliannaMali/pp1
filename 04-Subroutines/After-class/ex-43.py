def f(name):
    name = list(name)
    acronym = ""
    for num,i in enumerate(name):
        if num == 0:
            acronym += i
        if i == " ":               
            acronym += name[num+1]
    return acronym

if __name__ == '__main__':
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
    