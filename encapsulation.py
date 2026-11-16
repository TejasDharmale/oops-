# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance


# account1 = BankAccount(1000)
# account1.balance = -200
# print(f"Account balance: {account1.balance}")  # Output: Account balance: -200


# encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    @property  # getter property
    def get_balance(self):
        return self.__balance

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount >= self.__balance:
            raise ValueError(
                "Deposit amount must be less than the current balance.")
        else:
            self.__balance += amount
            print(f"Deposit successful: €{amount}")

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful: €{amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def show_balance(self):
        print(f"Current balance of account: €{self.__balance}")
        if self.__balance < 0:
            print("Balance cannot be negative.")
        else:
            print(f"Balance after withdrawal: €{self.__balance}")


user1 = BankAccount(1000)
user1.show_balance()
user1.deposit(500)
user1.withdraw(700)
user1.show_balance()  # Output: Balance: €1300
