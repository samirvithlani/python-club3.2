data = ([12,22,12],[23,45,33],[23,23,5])
sum =0
dailyavg =[]
for i in data:
    #print(i) #list
    for j in i:
        sum = sum+j
        print(j,end=" ")
    #print("sum = ",(sum//3))
    dailyavg.append(sum//3)    
    print()
    sum=0    

#print(dailyavg)    

max =dailyavg[0]

for i in dailyavg:
    if i> max:
        max =i

print("max",max)        


