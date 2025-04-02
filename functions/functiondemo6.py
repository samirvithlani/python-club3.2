def outer():
    x=100
    print("outer called...")
    def inner():
        y=200
        print("inner function",x)
    inner()
    

outer()        
