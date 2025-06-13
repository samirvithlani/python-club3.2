def sumofnos(*args):
    flag =True
    for i in args:
        if type(i).__name__ != "int":
            flag = False
            break
        
    if flag == True:
        return sum(args)
    else:
        return "not valuid..."
    


ans = sumofnos(1,2,3,4,5)
print(f"ans = {ans}")        