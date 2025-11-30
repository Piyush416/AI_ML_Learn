# JSON -> javascript object notation we use this formate to send the data 

# JSON   ->  Python
# Array  ->  List   (Array called in Json, list called in Python)
# Object ->  dict
# string ->  str
# null   ->  None
# true   ->  True

import json 

# ---------------------------------------------------------------
# json.loads() -> this function load the string json data into dict.  loads -> s means string
# json.dumps() -> this function convert the dict to string json data.  dumps -> s means string

# example

# json.loads()  -> convert json string to python dictionary
# we have json data in string formate.
json_str = '{"name": "piyush" , "age" : 21, "isStudent": true}'
print(type(json_str)) #output -> string
py_obj = json.loads(json_str)
print(type(py_obj) , py_obj)  #ouput -> dictionary


# json.dumps() -> dict convert into json string.
py_obj = {
    "name": "Piyush",
    "age" : 24,
    "isStudent" : True
}
json_str1 = json.dumps(py_obj)
print(type(json_str1), json_str1)

# ---------------------------------------------------------------
print("\n---------------------------------------------------------------\n")
# json.load() -> this function load json data into python dictionary
with open("/Users/piyush/Desktop/Python/5_python_file/4_json_module/4_sample.json", 'r') as f:
    py_obj1 = json.load(f)
    print(type(py_obj1), py_obj1)


# json.dump() -> this function dumps python dictionary to json data.
with open("/Users/piyush/Desktop/Python/5_python_file/4_json_module/4_sample.json", 'w') as f:
    data = {
        "name" : "Piyush",
        "isStudent" : True
    }
    json.dump(data, f, indent=4, sort_keys=True)


