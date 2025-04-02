def safe_divide(*args):
    return [(args[i]/args[i+1]) if args[i+1]!= 0 else "no is divisiable" for i in range(0,len(args),2)]
    #(args[i]/args[i+1]) // 10/2  if 2 is!= 0 
    #20,0
    #30

print(safe_divide(10,2,20,0,30,0))