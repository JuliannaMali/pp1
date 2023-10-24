grade1 = float(input("Enter grade: "))
def score(grade):
    while 1.0>grade>0.0:
        if grade>=0.9:
            return("A")
        elif 0.9>grade>=0.8:
            return("B")
        elif 0.8>grade>=0.7:
            return("C")
        elif 0.7>grade>=0.6:
            return("D")
        else:
            return("F")
print(score(grade1))        