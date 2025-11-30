'''Ask the user for a string and print:
• All unique characters
• The count of unique characters '''

user_str = input("Enter a String: ")

user_set = set()

for ch in user_str:
    user_set.add(ch)

# sort() function will return None
# mylist = list(user_set).sort() # in this line mylist store None because sort function will return none

mylist = list(user_set)
mylist.sort()
print(mylist)