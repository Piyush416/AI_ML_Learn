# The user enters a string containing into a number
# (e.g.,).Convert it to: "45"
# • an integer
# • a float
# • a string again
# Print all three values with their types

a = input("Enter a number: ")  #input taken is in string always.

integer = int(a)
floating = float(a)
string = str(a)

print(a, type(a))
print(integer, type(integer))
print(floating, type(floating))
print(string, type(string))


