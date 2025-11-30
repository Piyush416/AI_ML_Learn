'''Given a list of words :
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...} '''

words = ["apple", "banana", "kiwi", "cherry", "mango"]

dict = {}

for fruit in words:
    dict[fruit] = len(fruit)

print(dict)