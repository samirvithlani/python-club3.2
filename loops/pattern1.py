'''
*
**
***
****
*****
'''

#i -->row
#j -->col

# for i in range(1,6):#1 #2 #3 #4 #5 #6
#     for j in range(1,i+1): #1 -->6
#         print("*",end=" ")
#     print()    

# for i in range(1,6):#1 #2 #3 #4 #5 #6
#     for j in range(1,i+1): #1 -->6
#         print(i,end=" ")
#     print()        

# for i in range(1,6):#1 #2 #3 #4 #5 #6
#     for j in range(1,i+1): #1 -->6
#         print(j,end=" ")
#     print()    


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    


'''
1
23
456
78910
1112131415
'''
# k=1
# for i in range(1,6): #2 #3
#     for j in range(1,i+1):
#         print(k,end=" ") #4
#         k+=1 #2 #3 # 5 #
#     print()    

'''
0
01
010
0101
01010

1
10
101
1010
10101

'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end =" ")
    print()    