#data = {} # empty dictionary
data = {'name':'sachin','course':'python','fees':5000,'fees':6000}
print(data)
print(type(data))
data['name'] = 'sachin yadav'
# print(data['name'])
# print(data['course'])
# print(data['fees'])

data["duration"] = "2 months"
print(data)
data["course"] = "java"
print(data)

data.update({"location":"jaipur","fees":5000})
print(data)

#methods
k = data.keys()
print(k)
v = data.values()
print(v)
kv = data.items()
print(kv)


for k,v in data.items():
    #print(f"{k} = {v}")
    print(k,"=",v)
    
#remove data..

# removeditem = data.pop("location")
# print("removed item",removeditem)
print(data)    

removed = data.popitem()
print(data)
print(removed)