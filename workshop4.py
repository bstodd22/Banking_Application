class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        # Changes user's name
        self.name = new_name

    def change_pin(self, new_pin):
        # Changes user's pin
        self.pin = new_pin

    def change_password(self, new_password):
        # Changes user's password
        self.password = new_password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        # Shows user's balance
        print(f"Account Balance: ${float(self.balance):.2f}")

    def withdraw(self, amount):
        # Withdraws money from user's account
        if amount <= self.balance:
            # Decrements the user's balance
            self.balance -= amount
            print(f"Withdrawal successful! New Balance: ${float(self.balance):.2f}")
        else:
            print("Insufficient funds for withdraw.")

    def deposit(self, amount):
        # Deposits money into user's account
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New Balance: ${float(self.balance):.2f}")
        else:
            print("Invalid deposit amount.")

    def transfer_money(self, recipient, amount, pin):
        # Transfers money from one user's account to another user's account
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                print(f"Transfer successful. New Balance: ${float(self.balance):.2f}")
                return True
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Incorrect PIN. Transfer not allowed.")
            return False

    def request_money(self, recipient, amount):
        # User requests money from another user
        recipient_pin = int(input(f"Enter {recipient.name}'s PIN: "))
        if recipient_pin == recipient.pin:
            password = input("Enter your password to confirm the request: ")
            if password == self.password:
                self.balance += amount
                recipient.balance -= amount
                print("Money request and transfer successful.")
                return True
            else:
                print("Incorrect password. Money request denied.")
                return False
        else:
            print("Incorrect PIN. Money request denied.")
            return False


""" Driver Code for Task 1 """
"""if __name__ == "__main__":
    # Create instances of the User class
    user1 = User("Bob", 1234, "password")
    user2 = User("Alice", 1234, "password123")

    # Print the attributes of user1
    print("User 1:")
    print("Name:", user1.name)
    print("PIN:", user1.pin)
    print("Password:", user1.password)

    # Print the attributes of user2
    print("\nUser 2:")
    print("Name:", user2.name)
    print("PIN:", user2.pin)
    print("Password:", user2.password)"""

""" Driver Code for Task 2 """
"""if __name__ == "__main__":
    # Create instances of the User class
    user1 = User("Bob", 1234, "password")

    # Print the attributes of user1
    print("User 1:")
    print("Name:", user1.name)
    print("PIN:", user1.pin)
    print("Password:", user1.password)

    user1.change_name("Bobby")
    user1.change_pin(4321)
    user1.change_password("newpassword")

    print("User 1:")
    print("Name:", user1.name)
    print("PIN:", user1.pin)
    print("Password:", user1.password)"""

""" Driver Code for Task 3 """
"""if __name__ == "__main__":
    # Create instances of the BankUser class
    bank_user1 = BankUser("Bob", 1234, "password")

    # Print the attributes of bank_user1
    print("User 1:")
    print(f"Name: {bank_user1.name}")
    print(f"PIN: {bank_user1.pin}")
    print(f"Password: {bank_user1.password}")
    print(f"Balance: {bank_user1.balance}")"""

""" Driver Code for Task 4 """
"""if __name__ == "__main__":
    # Create instances of the BankUser class
    bank_user1 = BankUser("Bob", 1234, "password")

    # Call the methods of bank_user1
    bank_user1.show_balance()
    bank_user1.deposit(1000)
    bank_user1.show_balance()
    bank_user1.withdraw(500)
    bank_user1.show_balance()"""

""" Driver Code for Task 5 """
if __name__ == "__main__":
    # Create instances of the BankUser class
    bank_user1 = BankUser("Bob", 1234, "password")
    bank_user2 = BankUser("Madi", 529, "password1234")

    # Call the methods of bank_user1 and bank_user2
    bank_user2.deposit(5000)
    bank_user2.show_balance()
    bank_user1.show_balance()
    transfer_successful = bank_user2.transfer_money(bank_user1, 500, 529)
    if transfer_successful:
        print("Transfer successful.")
        # Request money from bank_user1
        request_successful = bank_user2.request_money(bank_user1, 300)
        if request_successful:
            print("Money request successful.")
        else:
            print("Money request failed.")
    else:
        print("Transfer failed.")
    bank_user2.show_balance()
    bank_user1.show_balance()
