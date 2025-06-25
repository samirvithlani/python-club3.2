class Bank:
    
    def balance(self):
        print("bank class balance method called..")


class ICICI(Bank):
    
    def balance(self):
        print("icici class balacne method called..")
        

i  = ICICI()
i.balance()
            
        
