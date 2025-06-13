# def getData():
#     yield [i for i in range(1,11)]
#     yield [i for i in range(11,21)]
#     yield [i for i in range(21,31)]
#     yield [i for i in range(31,41)]
#     yield [i for i in range(41,51)]

def getData(start, end, chunk_size):
    for i in range(start, end, chunk_size): #i=1,51,10
        yield list(range(i, min(i + chunk_size, end))) # 11011
        

# Example usage:
for chunk in getData(1, 101, 10):
    print(chunk)



# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in getData():
#     print(i)