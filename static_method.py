# class BankAccount:

#     bank_name = "ING Bank"

#     def __init__(self, username, balance):
#         self.username = username
#         self.balance = balance

#     @staticmethod
#     def is_valid_amount(amount):
#         return amount > 0

#     def deposit(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             self.balance += amount
#             print(f"Deposit successful: €{amount}")
#         else:
#             print("Invalid deposit amount!")

#     def show_balance(self):
#         print(f"Balance: €{self.balance}")


# # Creating account
# user1 = BankAccount("Tejas", 1000)

# # Depositing money
# user1.deposit(500)

# # Checking balance
# user1.show_balance()


###############################################################################################################################
class BankAccount:

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful: €{amount}")
        else:
            print(f"Invalid deposit amount! of {amount} for {self.username}")

    def show_balance(self):
        print(f"Balance of {self.username}: €{self.balance}")


user1 = BankAccount("Tejas", 1000)

user1.deposit(200)
user1.show_balance()

usere2 = BankAccount("John", 500)
usere2.deposit(-100)
