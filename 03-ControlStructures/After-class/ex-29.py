washing_product = str(input("Washing product: "))
rinse = str(input("Additional rinse (Yes/No): "))
spin = str(input("Additinonal spins (Yes/No): "))
total_time = 0
if rinse == "Yes" or rinse == "yes":
    total_time += 15
if spin == "Yes" or spin == "yes":
    total_time += 9
if washing_product == "jacket":
    total_time += 40
elif washing_product == "underwear":
    total_time += 70
elif washing_product == "shoes":
    total_time == 20

print(f'Total washing time is {total_time} minutes')