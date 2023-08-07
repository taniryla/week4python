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
        print(f"{self.name} has an account balance of: ${self.balance:,.2f}")

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

    def transfer_money(self, receiver_name, amount_to_transfer):
        # pin for the transferring user
        print(
            f"You are transferring ${amount_to_transfer:,.2f} to {receiver_name}")
        print("Authentication required")
        user_pin = input("Please enter your PIN number:")
        if user_pin == self.pin:
            print("Transfer authorized")
            print(
                f"Transferring ${amount_to_transfer:,.2f} to {receiver_name}")
            # balance of the user who is transfering the money
            self.balance -= amount_to_transfer
            # balance of the user who is receiving the money
            receiver_name.balance += amount_to_transfer
            return True
        else:
            return False

    def request_money(self, sender_name, amount_requested):
        # password for the user requesting money
        print(
            f"You are requesting ${amount_requested:,.2f} from {sender_name}")
        sender_pin = input(f"Enter {sender_name}'s PIN:")
        user_password = input("Enter your password:")
        if user_password == self.password and sender_pin == sender_name.pin:
            print("Request authorized")
            print(f"{sender_name} sent ${amount_requested:,.2f}")
            self.balance += amount_requested
            sender_name.balance -= amount_requested
            return True
        else:
            return False


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
"""
bankuser2 = BankUser("Chako", "2451", "chako123")
bankuser2.show_balance()
bankuser2.deposit(100)
bankuser2.show_balance()
bankuser2.withdraw(30)
bankuser2.show_balance()
"""

""" Driver Code for Task 5"""
bankuser2 = BankUser("Alice", "1234", "alice123")
bankuser3 = BankUser("Bob", "5678", "bob123")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser3.show_balance()
bankuser2.transfer_money(bankuser3, 500)
bankuser2.show_balance()
bankuser3.show_balance()
"""
if bankuser2.transfer_money(bankuser3, 500) == True:
    bankuser3.request_money(bankuser2, 200)
bankuser2.show_balance()
bankuser3.show_balance()
"""
