class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"The balance is: ${self.balance:,.2f}")

    def withdraw(self, withdrawal):
        # withdrawal = input("Enter amount to withdraw:")
        self.withdrawal = withdrawal
        self.balance -= withdrawal
        print(
            f"The withdrawal amount is ${withdrawal:,.2f} and the balance is ${self.balance:,.2f}")

    def deposit(self, deposits):
        # deposit = input("Enter amount to deposit:")
        self.deposits = deposits
        self.balance += deposits
        print(
            f"The deposit amount is ${deposits:,.2f} and the balance is ${self.balance:,.2f}")


""" Driver Code for Task 1 """

"""
client = User("Bob", "1234", "password")
print(
    f"Name is {client.name}, PIN is {client.pin}, and Password is {client.password}")
"""

""" Driver Code for Task 2 """
"""
client = User("Bob", "1234", "password")
print(
    f"Name is {client.name}, PIN is {client.pin}, and Password is {client.password}")
client.change_name("Bobby")
client.change_pin("4321")
client.change_password("newpassword")
print(
    f"Name is {client.name}, PIN is {client.pin}, and Password is {client.password}")
"""

""" Driver Code for Task 3"""
"""
bankuser1 = BankUser("Sara", "1245", "sarah123")
print(f"Name is {bankuser1.name}, PIN is {bankuser1.pin}, Password is {bankuser1.password} and balance is ${bankuser1.balance}")
"""

""" Driver Code for Task 4"""
bankuser2 = BankUser("Chako", "2451", "chako123")
bankuser2.show_balance()
bankuser2.deposit(100)
bankuser2.show_balance()
bankuser2.withdraw(30)
bankuser2.show_balance()
