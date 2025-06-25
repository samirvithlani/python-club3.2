from abc import ABC,abstractmethod
#abstract abse class

class Parent(ABC):
    
    @abstractmethod
    def comeHome(self):
        pass


class Child(Parent):
    
    def gohome(self):
        print("going home") 
    
    def comeHome(self):
        print("come home called....")           

c  =Child()
c.gohome()
c.comeHome()        
    
    