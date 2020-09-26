class GetSet:

    def __init__(self):
        
        self.value=0
        
    def getValue(self):

        print(self.value)

    def setValue(self,value):

        self.value=value

g1=GetSet()

g1.setValue(12)

g1.getValue()