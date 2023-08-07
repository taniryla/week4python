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

bankuser1 = BankUser("Sara", "1245", "sarah123")
print(f"Name is {bankuser1.name}, PIN is {bankuser1.pin}, Password is {bankuser1.password} and balance is ${bankuser1.balance}")
