distance = int(input('Enter distance in km: '))
hours = int(input('Enter number of travel hours: '))
minutes = int(input('Enter number of travel minutes: '))

avg_speed = lambda distance1,hours1,minutes1: round(distance1/(hours1+(minutes1/60)), 1)
result = avg_speed(distance, hours, minutes)

print(f'Average speed: {result} k/h')