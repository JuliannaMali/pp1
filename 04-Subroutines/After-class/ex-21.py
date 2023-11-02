import mymath
import mykeyboard

x = mykeyboard.read_number()
y = mymath.generate_number()
if x == y:
    print(f'Computer number: {y}')
    print("You won the game!")
else: 
    print(f'Computer number: {y}')
    print("You lost")