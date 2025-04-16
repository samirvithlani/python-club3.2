numbers = [12,22,23,1,34,56,67]
x = list(sorted(numbers))
print(x)

name = "ram"
x1 = sorted(name)
print(x1)

no = 178
strno = str(no)
listno = sorted(strno)
print(listno)
nolist = list(strno)
print(nolist)

if nolist == listno:
    print("true")
else:
    print("false")    


#["1","2","3"] --> no
#123 :map

#[even no ] [sqlist]


numbers = ["1","2","3"]

x = list(map(int,numbers))
print(x)

x1 = int("".join(numbers))
print(x1)