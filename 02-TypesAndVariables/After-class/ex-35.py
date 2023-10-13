import math
circumference = float(input("Enter tree circumference "))
diameter = circumference / (math.pi*2)
x = diameter >= 50

print(f"Tree can be cut down: {x}")