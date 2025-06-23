class Bank:
    
    def __init__(self,name):
        self.intrate = 8
        self.name = name
        print("bank class default const...")


class SBI(Bank):
    def __init__(self,name):
        super().__init__(name)
        print("SBI CLASS DEfault const..")
    
    def getIntRate(self):
        print(f"int rate = {self.intrate}")        



s = SBI("SBI")   
s.getIntRate()     