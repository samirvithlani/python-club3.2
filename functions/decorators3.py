

def orderFood(func): #func == throwParty()
    
    def inner(person):
        print("persons in inner",person)
        func(person*2) #throw{arty(100*2)}
        
    return inner    
        

@orderFood
def throwParty(person): #200
    print("giving party..",person)


throwParty(100)    