def compose(*functions):
    
    def composed_function(x): #string......
        for f in functions: #cleanData
            x = f(x) #x =convertLowe() 
        return x
    
    return composed_function    
            
    
def cleanData(text):
    print("clean data called...",text)
    return text

def convertLower(text):
    print("convert lower called...",text)
    return text.lower()
    
def remove_stop_words(text):
    #{the,at,in, a}
    print("stop words removing...",text)    
    return text

result = compose(cleanData,convertLower,remove_stop_words)
#resukt == composedFunction

result("hi thId is # India india *  at the 1st position in populATION")