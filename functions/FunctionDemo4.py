#args
def userName(*user):
    print(user)


userName("ram","shyam","hari")    

# def empNames(*emps,name):
#     print(emps)
#     print(name)
#empNames("amit","sumit",name="ram")    
def empNames(name,*emps):
    print(emps)
    print(name)

empNames("amit","sumit","ram")        
