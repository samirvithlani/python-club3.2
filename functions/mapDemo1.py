#map
data1 = [1,2,3,4,5]
data2 = [2,3,4,5,6]

# x = map(lambda x: x**3,data1)
# print(list(x))

x = map(lambda x,y : x+y,data1,data2)
print(list(x))

#[1,2,3,4,5]

data =[1,2,3,4,5]

#ans = map(lambda x: x +1,data)


#[1+2,2+3,3+4,4+5]

x = map(lambda x ,y: x + y, data1,data1[1:])
print(list(x))
