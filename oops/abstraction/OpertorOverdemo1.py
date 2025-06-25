class Test:
    
    def __init__(self,x):
        self.x = x
        
        print("Test class Default const called...")
    
    def __add__(self,other): #self t1 other t2
        print("add called...")    
        print(f"{self.x}")
        print(f"{other.x}")
        return self.x + other.x #10,100
    
    def __truediv__(self,other):
        print("true div called")
        return self.x  / other.x


t1 = Test(10)
t2 = Test(100)

#ans = t2 + t1
#print("ans = ",ans)

ans = t1/t2
print(ans)

        
        