class C():
    def __init__(self, x):
        self.x = x
    def m1(self):
        return self.x
    def m2(self):
        self.x+=1
    def m3(self):
        self.x-=1
    def m4(self,n):
        self.x+=n
    def __str__(self):
        return str(self.x)
    
c=C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
print(c.__str__())
