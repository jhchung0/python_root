class C(object):
    def __init__ (self,v):
        self.value = v
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v

        
c1 = C(10)
print ( c1.getValue())
c1.setValue(30)
print ( c1.getValue())




