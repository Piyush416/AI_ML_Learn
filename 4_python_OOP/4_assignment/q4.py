# concept -> function overriding
''' Create a class Shape  with a method area().
Create subclasses Circle, Rectangle , and Triangle that override the area() method. '''

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area of Circle with radius = {self.radius} is: {3.14*(self.radius**2)}")

class Rectangle(Shape):
    def __init__(self, l , b):
        self.l = l
        self.b = b
    def area(self):
        print(f"Area of Rectangle l = {self.l} and b = {self.b} = {self.l * self.b}")

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        print(f"Area of Triangle = {1/2 * (self.b) * (self.h)}")


circle = Circle(4)
rect = Rectangle(10,20)
triangle = Triangle(2,4)

circle.area()
rect.area()
triangle.area()