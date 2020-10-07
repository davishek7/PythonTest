class Calc:

    def Area(self,a=None,b=None):

        if a!=None and b!=None:
            return a*b

        elif a!=None:
            return a*a
            
        else:
            return 0

calc=Calc()

print(calc.Area())
print(calc.Area(4))
print(calc.Area(8,7))