# data=[]
# for i in range(1,11):
#     data.append(i)
    

# print(data)    

data = [i for i in range(1,11)]
print(data)

#comprehenion with cond

even_nos = [i for i in range(1,11) if i %2 ==0]
print(even_nos)

#["odd","even","odd",....]


data1 = ["even" if i % 2==0 else "odd"  for i in range(1,11)]
print(data1)

# for i in range(1,11):
#     if i %2 ==0:
#         data.append("even")
#     else:
#         data.append("odd")    

# print(data)        

fruits = ["apple","banana","mango","orange"]
filt = [ i for i in fruits if len(i)>5]
print(filt)

name = "jeet120part24jay100"
digits =[i for i in name if i.isdigit()]
print(digits)