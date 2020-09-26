class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def update(self):
        print("Age of {} is {}".format(self.name,self.age))
    
    def compare(self,other):
        if p1.age==p2.age:
            return True
        else:
            return False

p1=Person('Avishek',24)
p2=Person('Bubai',25)

if p1.compare(p2):
    print("They are same")
else:
    print("They are different")

p1.update()
p2.update()

    

