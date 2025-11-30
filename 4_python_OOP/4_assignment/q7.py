# Concept: Constructor Overloading (with Default Parameters)
''' Q7. Create a class Person that allows the constructor to work with:
• name only
• name + age
• name + age + address
As direct constructor overloading (multiple constructors) are not allowed but
we have to use default parameters to simulate constructor overloading. '''

class Person:
    def __init__(self,name,age = None,address=None):  #parameterize contructor if we use only self then it will be default contructor
        self.name = name
        self.age = age
        self.address = address
    
    def show(self):
        print(f"Hi, {self.name} {self.age} {self.address}")


p1 = Person("piyush")
p2 = Person("piyush", 21)
p3 = Person("piyush", 21, "Surat")
p1.show()
p2.show()
p3.show()
