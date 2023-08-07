class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password


class BankUser:
    def __init__(self):
        self.balance = 0
    super().__init__(User)

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
