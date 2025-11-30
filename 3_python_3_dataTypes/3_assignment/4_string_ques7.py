''' Write a program that takes a string from the user and prints the number of
spaces in the string. '''

user_str = input("Enter a String: ")

user_list = user_str.split(" ")
print(len(user_list)-1)

# -------------------------

count = 0
for ch in user_str:
    if ch == ' ':
        count+=1
print(f"total Space: {count}")