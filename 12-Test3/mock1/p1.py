def f(word):
    list1 = []
    i = 0
    while i < len(word):
        word = word.lower()
        x = list(word)
        x[i] = x[i].upper()
        list1.append("".join(x))
        i += 1
    return "-".join(list1)

print(f("book"))
print(f("water"))
print(f("ok"))
print(f("a"))
print(f(""))