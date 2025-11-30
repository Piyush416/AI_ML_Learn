''' Create a class Student with private attributes _name, _roll_no, and _marks.
Provide and methods with validation (e.g., marks cannot be
negative, roll number has to be between 1 & 100 & name cannot be empty). '''

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")

    def set_roll_no(self, roll_no):
        if roll_no >= 0 and roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("enter rollno in 1 to 100")
        
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("name cann't be empty")

    def get_name(self):
        print(self.__name)

    def get_marks(self):
        print(self.__marks)

    def get_rollno(self):
        print(self.__roll_no)


s1 = Student("Piyush", 23, 93)
s1.set_name("Rahul")
s1.get_name()

