name = "ram is asanatan"

# name = name.capitalize()
# print(name)

# name = name.title()
# print(name)

#name = name.upper()
#name = name.lower()

ind  = name.index('a') #1st
ind  = name.index('a',ind+1)
print(ind)

ind = name.find("s")
print(ind)


# #name = name.replace('a',"A")
# name = name.replace('a',"A",2)
# print(name)


# cnt = name.count('a',3)
# print("count = ",cnt)

email = "   ram@gmail.com  "
print(len(email))

#email = email.lstrip()
print(len(email))

email = email.strip()
#email = email.rstrip()
print(len(email))


x = email.split("@")
print(x)