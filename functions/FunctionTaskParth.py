
x = ["is","at","the"]

data = "hi this # is parth 1"

#x = ''.join(i for i in data if i.isalnum() or i.isspace())
x = " ".join(i for i in data.split() if i not in x)
print(x)