time = input("Enter time (24-hour format): ")
if time[2] == ":":
    hour = int(time[0:2])
    minutes = time[2:]
    if hour > 12:
        hour -= 12
        print(f'Time in 12-hour format: {hour}{minutes}pm')
    else:
        print(f'Time in 12-hour format: {hour}{minutes}am')
else:
    print(f'Time in 12-hour format: {time}am')