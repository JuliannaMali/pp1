recorded_speed= [48,47,54,50,42,68,39,46]

too_high = list(filter(lambda x: x>50, recorded_speed))

print(f'Speed too high: {too_high}')

