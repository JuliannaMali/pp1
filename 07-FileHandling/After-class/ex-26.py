import re
message = 'To be, or not to be, that is the question'
vowel = re.findall("['a''e''i''o''u']", message)
print(len(vowel))