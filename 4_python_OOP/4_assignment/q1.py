''' Create BankAccount class with attributes account_number , owner_name and balance.
Add methods to deposit, withdraw and check balance '''


class BankAccount:
    def __init__(self, number, name, balance, passcode):
        self.name = name
        self.number = number
        self.__balance = balance
        self.__passcode = passcode

    def deposit(self, amount, passcode):
        if(self.__passcode == passcode):
            if amount >= 0:
                self.__balance += amount
                print(f"Updated Balance: Rs.{self.__balance} of {self.name}")
            else:
                print("amount must be positive.")
        else:
            print("Incorrect Pin")
    
    def withdraw(self, amount, passcode):
        if self.__passcode == passcode:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Updated Balance: Rs.{self.__balance} of {self.name}")
            else:
                print("Insufficent Balance")
        else:
            print("Incorrect Pin")
    
    def check_balance(self, passcode):
        if self.__passcode == passcode:
            print(f"Available Balance: Rs.{self.__balance} of {self.name}")
        else:
            print("Incorrect Pin")

a1 = BankAccount(1, "piyush", 500, 4321)
a2 = BankAccount(1, "shree", 1000, 1234)

a1.deposit(500, 4321)
a1.withdraw(1000, 4321)
a1.check_balance(4321)

a2.deposit(-200, 1234)
a2.deposit(200, 1234)
a2.check_balance(1234)
a2.withdraw(800,1234)


