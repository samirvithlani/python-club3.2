#lambda functinos
#anon.. function...

#withour return type without argument lambda

x = lambda : print("hello")
x()

# def sum(a,b):
#     return a+ b

ans = lambda a,b: a+b
print("ans = ",ans(100,20))


#check user is valid or not

valid = lambda age: "valid" if age>18 else "not valid"
print(valid(100))


#only if

#valid1 = lambda age : if age >18 "valid"
valid1 = lambda age : age> 18 and "valid"
print("valid 1",valid1(12))

