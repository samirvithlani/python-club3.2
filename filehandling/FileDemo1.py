#open read/write close...

# file = open("./filehandling/demo1.txt","w")
# file.write("Hi this is first file but overrr.... ")
# file.close()

# with open("./filehandling/demo2.txt","a") as file:
#     file.write("Hello")


users = ["parth","jeet","jay","raj","rahul"]
with open("./filehandling/users.txt","w") as file:
    #file.writelines(users)
    #file.writelines(i for i in users)
    file.writelines(i +"\n" for i in users)
    print("data has been write..")
