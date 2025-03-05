#dictonary comprehension
d = {i: i**2 for i in range(1,10)}
print(d)

#if else in dictionary comprehension
d1 = {i:('even' if i%2==0 else 'odd') for i in range(1,10)}
print(d1)

users =["jay","jeet","parth"]
roles = ["admin","user","guest"]

users_role= {}
for i in range(len(users)):
    users_role[users[i]] = roles[i]
print(users_role)


#comprehension

users_role1 = {users[i]:roles[i] for i in range(len(users))}
print(users_role1)




