numbers = [1,2,3,4,5,6,7,8,9,10]

evennums = list(filter(lambda x:x%2 ==0,numbers))
print(evennums)


strings = ["hello","","world","","python"]
filtStrings = list(filter(None,strings))
print(filtStrings)

employees =[
    {
        "name":"ram","salary":50000
    },
    {
        "name":"shyam","salary":55000
    },
    {
        "name":"amit","salary":45800
    }
]

filtemployees = list(filter(lambda emp:emp['salary']>=50000,employees))
print(filtemployees)


langs =["Gujarati","hindi","english","marathi","malayalam"]
longNames = list(filter(lambda name:len(name)>5,langs))
print(longNames)



#filter with custome function...
#3
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        
        if n %i ==0:
            return False
    
    return True    
        

numbers = list(range(1,30))
print(numbers)


primes = list(filter(is_prime,numbers))
print(primes)
