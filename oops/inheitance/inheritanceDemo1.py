class Bank:
    
    def __init__(self):
        self.intrate = 8
        print("bank class default const...")


class SBI(Bank):
    def __init__(self):
        super().__init__()
        print("SBI CLASS DEfault const..")
    
    def getIntRate(self):
        print(f"int rate = {self.intrate}")        



s = SBI()   
s.getIntRate()     