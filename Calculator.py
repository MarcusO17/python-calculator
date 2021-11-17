number1 = float(input("Enter number 1 : "))
number2 = float(input("Enter number 2 : "))

option = input("Enter your operation type (+,-,*,/): ")

if option is "+":
    total = number1 + number2
if option is "-":
    total = number1 - number2  
if option is "*":
        total = number1 * number2     
if option is "/":
    total = number1 / number2  
    
print("Your total is " + str(total))
