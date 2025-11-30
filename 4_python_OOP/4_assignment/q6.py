# Concept: Abstraction
''' Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently. '''


from abc import ABC,abstractmethod

class Employee(ABC): # abstract class

    @abstractmethod  #decoder -> help developer to read faster
    def calculate_salary(self):  # abstract method
        pass


class Intern(Employee):
    def calculate_salary(self):
        print("Intern Salary:",20_000)

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("FullTimeEmployee Salary:",50_000)
    
class ContractEmployee(Employee):
    def calculate_salary(self):
        print("ContractEmpolyee Salary:",45_000)

piyush = Intern()
rahul = Intern()
shree = FullTimeEmployee()
laxman = ContractEmployee()

piyush.calculate_salary()
shree.calculate_salary()
laxman.calculate_salary()




        



