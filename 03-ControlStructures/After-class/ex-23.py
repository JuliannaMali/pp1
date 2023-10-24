dog_age = float(input("Enter the dog's age in human years: "))
years = 0
if dog_age <= 2:
    years += dog_age*10.5
else:
    years += ((dog_age-2)*4+2*10.5)

print(f"The dog's age in dogs years is {years} years")