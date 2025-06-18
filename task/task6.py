# Given a list and a target sum, return all unique pairs that add up to the target.
def find_pairs(data,x):
    found=[]
    for i in range(0,len(data)):#[1,2,3,4,5,6]
        for j in range(i+1,len(data)):#[2,3,4,5,6]
            if data[i]+data[j] ==x:
                found.append((data[i],data[j]))
                # foundTuple =(data[i],data[j]) #(1,6)
                # if foundTuple not in found:
                #     found.append(foundTuple)
    
    return found                
                
                
    

x = find_pairs([1, 2, 3, 4, 5, 6], 5)
print(x)
# Output: [(1, 6), (2, 5), (3, 4)]

