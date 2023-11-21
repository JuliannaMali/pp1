x = "An apple a day keeps the doctor away"
y = x.split()

#a
def amount_of_words(arr):
    x = len(arr)
    return x
#b
def shortest_to_longest(arr):
    def lenght(arr):
        return len(arr)
    x = arr.sort(key=lenght)
    return x
#c
def alphabetical(arr):
    x = arr.sort()
    return x

print(amount_of_words(y))
print(shortest_to_longest(y))
print(alphabetical(y))