import math
class shape:
    def __init__(self,color='black',field=False):
        self.color=color
        self.field=field
    def set_color():
        self.color
    def get_color():
        return self.color
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def are(self):
        return str(2*(self.length+self.breath))
    def parimetere(self):
        return (self.length*self.breath)
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def are(self):
        return (3.14*self.radius*self.radius)
    def parimetere(self):
        return (3.14*self.radius)
r1=rectangle(12,12)
c1=circle(3)
for i in(r1,c1):
    print ("are is",i.are())
    print ("parimetere is",i.parimetere())
    