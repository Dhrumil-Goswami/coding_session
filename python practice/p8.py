
class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def showdata(self):
        print("id:"+str(self.id))
        print("name"+str(self.name))
        print("salary"+str(self.salary))

n=input("enter number of employee detail you want to enter")
for i in range(n):
    id=input("enterid")
    name=raw_input("name:")
    salary=input("salary:")
    print("-----------------\n\n")

a=employee(id,name,salary)
a.showdata()

        