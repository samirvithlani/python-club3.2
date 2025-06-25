#compile time : method overloadin
    #same name method created in same class with diff argument
#runtim poly  : method overriding
    #same name emthod create in child class with same signature called method overriding

class User:
    
    def getData(self,name,age):
        print(f"name = {name} age = {age}")    
        
    def getData(self,name):
        print(f"Name = {name}")    
       


u = User()
u.getData("jay")        
