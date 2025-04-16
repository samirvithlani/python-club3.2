values = [True,True]
print(all(values))

values =[]
print(all(values))


numbers = [1,2,3,4,0,-1]
print(all(values))

strings = ["","world"]
print(all(strings))

data = [21,22,19,20]
print(all(i>18 for i in data))
