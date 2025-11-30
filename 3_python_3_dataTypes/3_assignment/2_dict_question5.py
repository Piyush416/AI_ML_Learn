''' Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks '''

dict = {}


while True:

    print("A - Add a student \nB - Update marks \nC - Search for a student \nD - Display all students and marks\nE - To exit Program")

    user_request = input("Select Option To Perform: ").lower()

    match user_request:
        case 'a':
            std_name = input("Enter Student Name: ").lower()
            std_marks = int(input("Enter Student Marks: "))
            if dict.get(std_name) == None:
                dict[std_name] = std_marks
                print(f"{std_name} and {std_marks} added Successfully.")
            else:
                print(f"{std_name} Student is already exist.")

        case 'b':
            std_name = input("Enter Student Name: ").lower()
            std_marks = int(input("Enter Student Marks: "))
            if dict.get(std_name) != None:
                dict[std_name] = std_marks
                print(f"{std_name} Student Marks Updated Successfully.")
            else:
                print(f"{std_name} Student is not exist in record.")
        case 'c':
            std_name = input("Enter Student Name: ").lower()
            if dict.get(std_name) != None:
                print(f"{std_name} : {dict[std_name]}")
            else:
                print(f"{std_name} Student not exist in record.")
        case 'd':
            print(dict)
        case 'e':
            print("To exit Program")
            break
        case _:
            print("Enter Valid Operation(A,B,C,D)")
        






