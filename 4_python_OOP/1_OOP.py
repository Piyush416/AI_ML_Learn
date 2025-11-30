# OOP -> object oriented programming -> class/object we have
# class -> blueprint of object
# object -> instance of class



# ------------------------------------------------------------------------
# Intro of class and object
class Student:
    course = "Python"  # class attribute
    PI = 3

    def __init__(self,name,cgpa):    # constructor
        self.name = name  # instance attribute  - for each object it will be store in RAM while class attribute will not 
        self.cgpa = cgpa  # instance attribute
        self.PI = 3.14


st1 = Student("Piyush", "9.8")  # this "()" indicate that we call the constructor function.
print(f"{st1.name} and {st1.cgpa} and {st1.course} and {Student.course}")  # object can access class attribute 
print(st1.PI)  # object attribute will be access first because object have highest priority 
print("\n")

# ------------------------------------------------------------------------
# Types of Methods

class Laptop:
    storage_type = 'ssd'

    def __init__(self, ram, storage):   
        self.ram = ram
        self.storage = storage

    @classmethod  #decorator  define the below function that this is class function
    def get_storage_type(cls):  # in class function we use cls as first parameter
        print(f"Storage Type = {cls.storage_type}")

    def get_info(self): # instance method we always use self as first parameter
        print(f"laptop has {self.ram} & {self.storage} {self.storage_type}")
    
    @staticmethod  # don not have access of class or instance attribute
    def discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price : {final_price}")
    
l1 = Laptop("16gb", "512gb")
l1.get_info()
l1.discount(40_000,10) # integer ignore _ , we use only for big number to read faster 40thousand.
Laptop.get_storage_type()
l1.get_storage_type()
    