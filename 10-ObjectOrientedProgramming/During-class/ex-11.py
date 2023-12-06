class TV():
    def __init__(self):
        self.is_on=False
    def tv_turned_on(self):
        self.is_on=True
    def tv_turned_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print('TV is on')
        else:
            print('TV is off')

tv=TV()
print(tv.show_status())
tv.tv_turned_on()
print(tv.show_status())
tv.tv_turned_off
print(tv.show_status())
