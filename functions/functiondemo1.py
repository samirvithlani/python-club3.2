def test():
    print("Hello from functiondemo1.py")
    
def test2()->None:
    print("Hello from functiondemo1.py")    
    

def avg(a,b):
    c = (a+b)/2
    print(c)

avg(100,200)        

def avg1(a:int,b:int)->None:
    print("a:",a)
    print("b:",b)
    #c = (a+b)//2
    #print(c)

avg1(100.20,200.200)    
avg1("Hello","World")

test()    
test2()