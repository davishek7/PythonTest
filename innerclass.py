class Student:

    def __init__(self,name,age):

        self.name=name
        self.age=age
        #self.lap=self.Laptop()

    def show(self):

        print(self.name,self.age)

    class Laptop:

        def __init__(self,brand,ram,cpu):

            self.brand=brand
            self.ram=ram
            self.cpu=cpu

        def show(self):

            print(self.brand,self.ram,self.cpu)

s1=Student("Avishek",24)
s1.show()
l1=s1.Laptop("Asus",4,"i3")
l1.show()