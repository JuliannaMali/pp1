arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
word_lenght =[]
for x in arr:
    word_lenght.append(len(x))
longest_word=[]
for x in arr:
    if len(x) == max(word_lenght):
        longest_word.append(x)
print(f'The longest word in array {arr} is {"".join(longest_word)}')