''' Q10. Take a decimal number as input (like 45.78) and output its:
integer part - 45
fractional part - .78 '''

a = float(input("Enter a decimal number: ")) # 45.78

integerPart = int(a)
decimalPart = float(a) - integerPart
print(integerPart)
print(decimalPart)


nums = input("Enter a decimal number: ") # 45.78
intPart , deciPart = nums.split(".")
print(intPart)
print(deciPart)


