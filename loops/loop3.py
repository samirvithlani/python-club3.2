#fibbonaci sears

a = 0 
b = 1
c = 0
print(a)
print(b)
for i in range(1,10):
    c=a+b # 0 + 1 = c , 1 + 1 ,1 + 2 ,3+2
    print(c,end=" ") #1 #2 #3 5
    a = b # a = 1, a= 1, a=2 ,a =3
    b = c # b = 1  b =2 ,b =3, b=5
    
    