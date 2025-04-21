no1 = int(input("enter no 1"))
no2 = int(input("enter no 2"))


def safeDiv(func):
    
    def inner():
        if no2 != 0:
            func()
        else:
            print("can not divide by zero.")    
    
    return inner        


@safeDiv
def div():
    print("div called...")
    ans = no1 // no2
    print("ans...",ans)

div()    