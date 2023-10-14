score = input("Enter score(from 0.0 to 1.0): ")
try:    
    if 0.0<= float(score) <= 1.0:
        if 1.0 >= int(score) >= 0.9:
            print("A")
        elif 0.9 > int(score) >= 0.8:
            print("B")
        elif 0.8 > int(score) >= 0.7:
            print("C")
        elif 0.7 > int(score) >= 0.6:
            print("D")
        elif 0.6 > int(score):
            print("F")
    else:
        print("Invalid score")
except:
    print("Invalid score")