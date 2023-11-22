name="Anna May"
uni = "Cracow University of Economics"
field = "Applied Informatics"

file = open("students.txt", "w")
file.write(name+"\n")
file.write(uni+"\n")
file.write(field+"\n")
file.close()