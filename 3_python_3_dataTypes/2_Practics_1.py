'''
Give a list of tuples with info(name , subject):
1. list all the unique course
2. list students enrolled in English
3. create dictionary(student, set of courses)
'''
info = [
    ("Alice" , "Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math"),
    ("Alice" , "English"),
    ("Charlie" , "English")
    ]


# 1. list all the unique course
unique_course = set()
for tuple in info:
    unique_course.add(tuple[1])
print(unique_course)
    
    
# 2. list students enrolled in English
list = []
for name,course in info:
    if course == "English":
        list.append(name)
print(list)
        

# 3. create dicttionary(student, set of courses)
dict = {}
for name,course in info:
    if dict.get(name) == None:
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
