class complexnumber:
    attr=0
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def getData(self):
        print("{0}+{1}".format(self.real,self.imag))
c1=complexnumber(2,3)
c1.getData()
print(c1.attr)
c2=complexnumber(5)
print(c2.attr)
c2.attr=10
print((c2.real,c2.imag,c2.attr))

