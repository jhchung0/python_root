class C(object):
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subrtract(self):
        return self.a - self.b


C1 = C(10,15)

print(C1.add())


