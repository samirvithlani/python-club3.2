#const defination

class Bank:
    
    def __init__(self):
        print("bank class def const calle...")
        self.name = "ICICI"
        self.city = "ahmedabad"
    
    def getBannkDetail(self):
        print(f"bank name - {self.name} city = {self.city}")    


b = Bank() #bank class default const called...        
b.getBannkDetail()    