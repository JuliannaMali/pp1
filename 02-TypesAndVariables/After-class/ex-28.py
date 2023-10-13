height = int(input("Input your height in cm: "))
weight = int(input("Input your weight in kg: "))
bmi = round(weight/(height/100)**2, 2)
x = 24.99 > bmi > 18.5
print(f'Your BMI index: {bmi}')
print(f'Correct weight: {x}')