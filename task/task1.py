scores =[["virat",10,20,30,40,50],["ms",90,89,70,0,10],["hardik",100,20,30,40,60]]
finalScore=[]
sum=0
for i in range(0,len(scores)):
    for j in range(1,len(scores[i])):    
        sum = sum+scores[i][j]   
    finalScore.append([scores[i][0],sum])
    sum=0
print(finalScore)    