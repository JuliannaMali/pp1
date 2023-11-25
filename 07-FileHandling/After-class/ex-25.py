message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
import re
temp = re.findall('\d''\d', message)
x = ' '.join(temp)
print(x)