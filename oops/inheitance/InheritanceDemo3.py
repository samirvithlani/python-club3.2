class Father:
    def __init__(self):
        print("Fater const called....")
    

class Mother:
    def __init__(self):
        print("mother const callled...")

class Child(Mother,Father):
    def __init__(self):
        super().__init__()


c = Child()