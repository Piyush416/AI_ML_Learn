# OOPs have 4 pillar 
# 1. encapsulation -> wrapping data & function into single unit.
# 2. Abstraction -> hiding internal details and showing only essential features
# 3. inheritance -> Reusing attribute & methods from a Parent(Base) Class
# 4. polymorphism -> object should have more than one behaviours.


# Encapsulation -> Wrapping data & function into single unit.
# same as class -> attribute and methods are group together and form class same encapsulation
# by using this we can perform data hiding

# data hiding
# attribute version
# 1. public -> access in or outside the class by default public attribute is created
# 2. protected -> access in class and sub_class only. (in python it is not forcefully we can access it outside the class also)
# 3. private -> access in class only.(same this also access outside the class but by naming we can understand it.)

class Banking:

    def __init__(self,name, balance, passcode):
        self.name = name #public
        # self._balance = balance #protected
        self.__balance = balance #private -> using getter and setter method we can access and update the private attribute
        self.__passcode = passcode

    def get_balance(self, passcode): #getter
        if passcode == self.__passcode:
            print(self.__balance)
        else:
            print("incorrect passcode")
    
    def set_balance(self, update_balance,passcode): #setter
        if passcode == self.__passcode:
            self.__balance = update_balance
            print(f"updated_balance is: {self.__balance}")
        else:
            print("invalid passcode")

p1 = Banking('piyush', 10_000, 4321)

# protected attribute accessing
# print(p1.name , p1._balance) # accessing protected attribute in python it is not forcefully 

# private attribute accessing
# print(p1.name , p1.__balance)  # not access this because it is private
print(p1.name , p1._Banking__balance) # with this we can access private attribute in python

passcode = int(input(f"Enter the 4 digit passcode of {p1.name} account: "))
p1.get_balance(passcode)

update_balance = int(input("Enter new balance: "))
p1.set_balance(update_balance, passcode)
