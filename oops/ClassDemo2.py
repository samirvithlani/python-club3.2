class BGMI:
    
    def map(self,pname):
        self.size = "10*10" #instance variable #101
        self.name  ="erangle" #101
        color = "gteen"
        self.pname = pname

    def play(self):
        print(f"playing BGMI map = {self.name} = size = {self.size} player = {self.pname} ") #101

b1 = BGMI()
b1.map("jeet")       #101
b1.play()      #101


b2 = BGMI()
b2.map("jay")
b2.play()