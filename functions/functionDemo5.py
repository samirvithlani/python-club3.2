#def getUserData(**kwargs,x): compile error
def getUserData(**kwargs):
    print(kwargs)
    


getUserData(name='John', age=25, city='New York')    



def printUserData(*args, **kwargs):
    print(args)
    print(kwargs)


printUserData('John', 25, 'New York', name='John', age=25, city='New York')    