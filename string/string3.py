#check string is palindrome or not:
name ="naman"
revname= ""
# for i in name:
#     revname = revname +i


for i in range(len(name)-1,-1,-1):
    revname = revname + name[i]

if name == revname:
    print("palindrome")
else:
    print("not palindrome..")    
    
    
name = "jeet jivani"    
flag = False
for i in name:
    if i == " ":
        #print("name has space")
        flag = True
        break

if(flag):
    print("name has sapce")


name = "amit patel ok java"
#amitpatelokjava
    
newname = ""    

for i in name:
    if  i != " ":
        newname = newname + i

print(newname)        
    
    
    

    


