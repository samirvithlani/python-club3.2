#database...
users = {"name":"ram","age":23,"role":"manager"}
#users={}

def isLogin(func):
    
    def inner(user):
        if len(users)>0 and users["name"]==user["name"]:
            func(user)
        else:
            print("redirecting to login page...")
                
     
    return inner       

@isLogin
def home(user):
    print("logged in user = ",user)


home({"name":"rami","age":23,"role":"manager"})
    
    

        
        