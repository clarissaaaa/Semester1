def factorial (number) :
    if number > 1 :
        print(number)
        return number * factorial(number-1) 
    else:
        return number
    
factorial(10)