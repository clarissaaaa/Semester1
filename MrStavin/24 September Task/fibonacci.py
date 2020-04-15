def fibonacci (n):
    a = 0 
    b = 1
    if n<0:
        print ("Invalid ")
    elif n==1 :
        return b 
    elif n==0 :
        return a
    else :
        for i in range(2,n):
            c= a+b 
            a=b
            b=c
        return b 
    
print(fibonacci (6))
    
#%%
#Method2
def fibonacci(number):
    if number  >1 :
        return fibonacci (number-1) + fibonacci(number-2)
    else: 
        return number
        
print (fibonacci(5))