no = int(input("eneter no to find fac.."))

fact =1
# for(int i=1;i<=no;i++){
#     fact = fact *i
# }
for i in range(1,no+1):
    fact = fact *i

print(fact)    