# Inheritance -> Reusing attribute & methods from a Parent(Base) Class

# Types of inheritance 

# 1. single level inheritance
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, course):
#         self.course = course

# t1 = Teacher("math")
# t1.change_time("5pm")
# print(t1.course, t1.start_time, t1.end_time)


# 2. multi level inheritance
# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)  #super() will call the parent class constructor
#         self.salary = salary


# acc1 = Accountant(25_000, "CA")
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)



# 3. multiple inheritance 
class Teacher:
    def __init__(self, salary):
        self.salary = salary
    
class Student:
    def __init__(self, subject):
        self.subject = subject
    
class TA(Teacher, Student):
    def __init__(self,salary, subject, name):
        super().__init__(salary) 
        Student.__init__(self, subject)
        self.name = name

ta1 = TA(9.3, "python", "piyush")
print(ta1.name, ta1.salary, ta1.subject)





