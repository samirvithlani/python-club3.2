def check(str1,str2):
    flag = False
    rev1 = str1[::-1]
    rev2 = str2[::-1]
    if rev1 == str1 and rev2 == str2:
        flag = True
    
    return flag    


x = lambda str1,str2 : str1 + str2 if check(str1,str2) else None
print(x("madam","jay"))