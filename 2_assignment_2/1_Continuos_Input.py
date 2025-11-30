# Design a program to continuously input a number from the user and print if it is positive or negative until the user enters “Quit”.

def take_input_game():
    while True:
        user_input = input("Enter a number(Type \"Quit\" for exit): ")
        if(user_input.lower() == "quit"):
            break
        try:
            if(int(user_input) >= 0):
                print("Positive")
            elif(int(user_input) < 0):
                print("Negative")
        except:
            print("Please Enter Valid Input")

take_input_game()
