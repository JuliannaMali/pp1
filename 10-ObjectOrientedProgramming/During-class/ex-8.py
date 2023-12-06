class Phone():
    def __init__(self,os,colour,number):
        self.os=os
        self.colour = colour
        self.number= number
        self.in_call= False
        self.restart=False
    def in_call(self):
        self.in_call=True
    def not_in_call(self):
        self.in_call=False
    def restart(self, true_or_false):
        self.restart= true_or_false
phone=Phone('Android','Black', 123123123)
print(f'Phone OS: {phone.os}')
print(f'Colour: {phone.colour}')
print(f'Number: {phone.number}')


if phone.in_call:
    print(f'This phone is currently in a call')
else:
    print('This line is free')

print(f'Would you like to restart the phone: {phone.restart}')
