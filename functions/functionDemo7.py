# #higher order function

# def add():
#     print("add called...")
# def sub():
#     print("sub called...")    
    
# def calc(func):
    
#     print("function called...")
#     func()


# calc(add)    

    
    
#higher order function

def add(a,b):
    return a +b
def sub(a,b):
    return a -b
    
    
def calc(func,a,b):
    
    print("function called...")
    x = func(a,b)
    print("ans = ",x)


calc(add,10,20)
calc(sub,100,20)

        