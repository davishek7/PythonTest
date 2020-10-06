class Calc:

    def __init__(self,m1,m2):

        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):

        m1=self.m1+self.m2
        m2=other.m1+other.m2

        return m1,m2
    
    def __gt__(self,other):

        r1=self.m1+self.m2
        r2=other.m1+other.m2

        if r1>r2:
            return True
        else:
            return False

    def __sub__(self,other):
        
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        s3=0
        if s1>s2:
            s3=s1-s2
        else:
            s3=s2-s1
        
        return s3

c1=Calc(12,10)
c2=Calc(14,16)

if c1>c2:
    print("c1 wins")
else:
    print("c2 wins")

c3=c1+c2
print(c3)

c4=c1-c2
print(c4)

