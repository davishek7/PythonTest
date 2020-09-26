class A:
    def __init__(self):
        print("In init A")

class B:
    def __init__(self):
        print("In init B")

class C(A,B):
    def __init__(self):
        print("In init C")
        super().__init__()          #in multiple inheritance when we call the init method of the super class the left most class will be given preference

c1=C()
