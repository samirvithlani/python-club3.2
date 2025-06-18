
with open("./filehandling/employee.txt","w") as file:
    while True:
        choice = input("enter your name or exit(for exit)")
        if choice == "exit":
            break
        
        age = int(input("enter age :"))
        city = input("enter city : ")
        
        file.write(f"Name ={choice} Age = {age} City={city}\n")
        print("data has been written !!")

        
        
        
        
    
    