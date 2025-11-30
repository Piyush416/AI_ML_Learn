# Excepiton Handling

try:
    x = int(input("Enter a Number: "))
    ans = 10/x

except ZeroDivisionError:
    print("Divide with zero is not possible")

except ValueError:
    print("Only Number is take in input")

# else will execute if try have no error
else:
    print(f"ans = {ans}")

# this will execute even after except 
finally:
    print("End of the program")