
def calculator():
    

    while True:
        first = int(input("Enter first Number"))
        operator = str(input("Enter operator"))
        second = int(input("Enter second Number"))


        if operator == "+" :   
            print(first + second)
        elif operator == "-":
            print(first - second)  
        elif operator == "*":
            print(first * second)
        elif operator == "/":
            print(first / second)  
        elif operator == "^":
            print(first ** second)     
         
calculator()            
    
    
    

    
    


