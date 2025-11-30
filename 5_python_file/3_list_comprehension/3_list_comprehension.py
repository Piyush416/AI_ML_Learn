# List Comprehension

# it is a way to do work in single line

# based on task we have different list comprehension
# syntax 1. -> [output iteration(loop) condition]

# Task1. create a list of sqaure of first 5 number
square = [i*i for i in range(6)]
print(square)

# only square of odd number of till 5
square = [i*i for i in range(6) if i%2 != 0]
print(square)


# Syntax 2.
# Task2. we have a list of positive and negative number replace -ve number with zero
nums = [-2,-3,4,5,6,-7]
nums = [0 if val < 0 else val for val in nums]
print(nums)


# Syntax 3.
# Task3. we have a string of list in lower case do it into uppercase
words = ["hello", "world", "python"]
words = [val.upper() for val in words]
print(words)