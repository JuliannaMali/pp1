distance = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))

def avg_speed(distance1, hours1, minutes1):
    time = hours1+minutes1/60
    return round((distance1/time), 1)

print(avg_speed(distance, hours, minutes))
