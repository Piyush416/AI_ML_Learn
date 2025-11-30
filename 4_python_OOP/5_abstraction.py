# Abstraction -> hiding internal details and showing only essential features.

# There is major difference between data hiding and abstraction
# data-hiding => hiding data (security)  using public private and protected 
# abstraction => hiding implementation(simplicity)

from abc import ABC,abstractmethod

class Animal(ABC):  # abstract class 
    @abstractmethod
    def make_sound(self): #abstract method
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()
