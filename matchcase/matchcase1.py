season = input("enter season")



match season:
    case "summer":
        print("this is summer season")
    case "winter":
        print("this is winter seaason")    
    case "monsoon":
        print("this is monsoon season")
    case _:
        print("please enter valid value...")
        