class FreeFire:
    
    gameName = "FF" #class level variable....
    
    #instance function
    def guildTest(self): #self == f
        print("FireFire Guild Test Failed...")
        print(self)
        #print(self.gameName)
        print(FreeFire.gameName)
        
        


f = FreeFire()
f.guildTest() #f.guildTest(f)        
print(f)
print(f.gameName)
