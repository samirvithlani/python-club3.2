
# try except
try:
    no1 = int(input("enter no 1"))
    no2 = int(input("enter no 2"))
    ans = no1 / no2
    print("ans = ",ans)


        
except ZeroDivisionError as e:
    print("can not divide by zero")    

except ValueError:
    print("check input...")    

except Exception as e:
    print("all exception...",e)    