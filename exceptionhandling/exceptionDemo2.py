age = int(input("enter age"))

try:
    if age<18:
        raise ValueError("please enter age grt>18")
except ValueError as e:
    print(e)    