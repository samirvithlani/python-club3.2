#wihout chaing in function : function control flow chnage ..
#decorators denboted by @
#decor.. working like Higher order function it will accept function argument...in param..

def orderFood(func): #func == throwParty #3
    print("ordering...")
    
    def inner(): #5
        print("inner...")
        func() #throwParty.. #6
    return inner     #function plus return #4
        
        


@orderFood #2
def throwParty():#7
    print("party throwing....") #8


throwParty()  #1  