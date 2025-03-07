#set  -->unique elements
#set is mutable
#set is unordered
#set is unindexed
#set is iterable
#set is not subscriptable
#set is not sliceable
#set is not repeatable
#set is not comparable
#set is not hashable
#set is not sortable


#[],{},(),set{}

data = set({10,20,30,40,50,100,60,70,80,90,100})
print(data)

data.add(200)
print(data)

#data.remove(100)
#data.discard(100)
x = data.pop()
print("removed elem =",x)
print(data)

data.update({100,200,300,400,500})
print(data)
