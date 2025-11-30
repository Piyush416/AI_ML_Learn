# Let’s create a simple calculator that performs arithmetic operations. Create a function that performs addition, subtraction, multiplication, or division based on the parameter.
# Calculator — calculator(a, b, operation)
# The operation parameter can have values: '+', '-', '*', '/'.

def calculator(a,b,operation):
    match operation:
        case '+':
            return a+b 
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return int(a/b)   # / operation give float value in result
        case _:
            print("give operation(+,-,*,/) in this : ")


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    operation = input("Enter Operation: ")
    
except ValueError:
    print("Enter a Number only.")

else:  # if try have no error then execute else code
    print(calculator(a,b,operation))




