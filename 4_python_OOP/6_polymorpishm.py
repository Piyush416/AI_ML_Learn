# Polymorphism -> many forms

# Example '+' operator is polymorphism
print(1+2 , "hello"+"world")  # add number and string both are different but working is same.


# Polymorphism types
# 1. Function Overriding (work in inheritance)
# we have parent class having function and we have child class having same function we overide this function

# class Employee:
#     def get_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.get_designation()


# 2. duckTyping
# we have two different classes and both have same name function that is call duckTyping
class Teacher:
    def get_designation(self):
        print("designation = Teacher")

class Accountant:
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()