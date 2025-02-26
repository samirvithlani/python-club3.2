data = ("ram","shyam","shiv","parvati")

#data[0] = "RAM"
#print(data.index("shiva"))
#print(data.count("shyam"))

print(data)

ListData = list(data)
print(ListData)
ListData.append("kumar")
data = tuple(ListData)
print(data)


a = ("amit","sumit")
b = ("parth","jay")

c =  a + b
print(c)
