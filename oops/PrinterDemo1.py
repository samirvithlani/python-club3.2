class Bank:
    
    def __init__(self,name,bal):
        self.name = name
        self.bal = bal
    def __str__(self):
        return f"Name = {self.name} balance = {self.bal}"
        
    

class Printer:
    
    @staticmethod
    def printUserData(bank):
        # print(f"user name = {bank.name}")
        print(bank)


names = ["jay","raj","parth"]        
amount =[10000,12000,20000]

bank = [Bank(n,b) for n,b in zip(names,amount)]
for i in bank:
    Printer.printUserData(i)
    
