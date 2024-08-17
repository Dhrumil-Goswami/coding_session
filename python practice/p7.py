l=[1,2,3,4,5,6,7]
print {i:i*i for i in range(5)}
class abc:
    def dhru(self,x,y,z=0):
        A= x-y+z
        print A
class cd(abc):
    def dhru(self,x,y):
        b=x+y
        print self.dhru
        print b
        
# e=cd()
# e.dhru(2,3)
# import random
# list1 = random.sample([i for i in range(random.randint()) if i %5==0 and i %7==0], 1)
# print(“Random Number divisible by 5 and 7”,list1)


