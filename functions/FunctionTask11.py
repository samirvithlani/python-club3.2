def getData(type1,**kargs):
    data={}
    for i,j in kargs.items():
        if type(j) ==type1:
            data[i]=j
    
    return data        
    

print(getData(int,a=10,b=20,x="ok",d=[1,2]))



#args
#[1,2,3],[2,3,4] -->1,4 - 5

def addData(*args):
    pass

addData([1,2,3],[2,3,4])