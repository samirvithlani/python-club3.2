def findMax(data):
    max = data[0]
    for i in data:
        if i > max:
            max = i
            
    return max

x = findMax([1, 2, 3, 4, 5])
print(x)
