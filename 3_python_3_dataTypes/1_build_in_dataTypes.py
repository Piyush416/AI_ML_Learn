# in python there is 4 main build in datatypes list, tuple, dictionary, set

# List
# 1. Mutable in Nature -> means at index we can change value list[2]
# 2. any data can be store 
# 3. use [] we can make it
# ex. list = [1,2,3,4,5,"Piyush",3.14]


# Tuple 
# 1. immutable in Nature -> means we cannot change value at index
# 2. any data can be store 
# 3. use () we can make it
# ex. list = (1,2,3,4,5,"Piyush",3.14)
# PLUS POINT 
# single tuple we want tuple = (1,) we have to use "," after that otherwise it will assume "(1)" this is simple integer.
# tuple = ("abc")
# print(type(tuple))  #output -> string


# Dictionary
# 1. Mutable in Nature -> means at key we can change value 
# 2. data store in key value pair 
# 3. use {} we can make it
# Ex. dic = {"name" : "Piyush", 3.14 = "PI"}
# PLUS POINT
# dic["age"] give error that key not found and stop the program.
# dic.get("age") this will give None and program run till end.


# Set -> it store unique value 
# 1. Set is mutable but elements of set is immutable means immutable can be store like -> tuple, string, mutual element is not store like list and dic
# 2. any data can be store 
# 3. use {} we can make it
# ex. set = {1,2,2,2,3,2,2} len = 3(unique element only)
# PLUS POINT
# empty_set = {} -> python understand this is dictionary
# so we use constructor empty_set = set() 

