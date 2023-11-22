movies = ['Silence of th Lambs', "Voices", "The Eye", "The Blair Witch Project", "Old Rites"]
file = open("movies.txt", "w")
for x in movies:
    file.write(x+"\n")

file.close()