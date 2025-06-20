class Veh:
    
    def __init__(self,name,price,type):
        self.name = name
        self.price = price
        self.type = type
    
    
    def getVehData(self):
        print(f"veh name  = {self.name}")
        print(f"veh price  = {self.price}")        
        print(f"veh type  = {self.type}")                


v = Veh("AUDI",12000,"CAR") 
v.getVehData()

v1 = Veh("ACIVA",1200,"VEHICLE") 
v1.getVehData()       
        
    