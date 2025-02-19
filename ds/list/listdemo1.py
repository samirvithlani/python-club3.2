users =[]
print(users)
print(type(users))

users = ["java","python","c","cpp"]
print(users)
users[0] ="JAVA"
print(users)
print(users[0])

# for i in range(0,len(users)):
#     print(users[i])


# for i in users:
#     print(i)
    
users.append("JS")    
#users.extend(["php",".net"])
users.extend("PHP")
#users.remove("JAVA")    
#removedELm = users.pop()
removedELm = users.pop(2)
print("removing...",removedELm)
print(users)

    