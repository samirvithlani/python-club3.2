class Veh:
    
    className = "VEHICLE" #class...
    
    def startVeh(self):
        self.engine = "v8" #instance variable...
        key = "auto"
        print("starting veh.....")
        
    

class Car(Veh):
    
    def startCar(self):
        self.startVeh()
        print("starting car...",Veh.className,self.engine)
        


audi = Car()
#audi.startVeh()
audi.startCar()        
    