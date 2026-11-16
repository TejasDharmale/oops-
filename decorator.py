import datetime


class User:
    def __init__(self, password, email, username):
        self.password = password  # public attribute
        # private attribute because of the underscore prefix which make it secured
        self._email = email
        self.username = username  # public attribute

    @property
    def email(self):
        allowed_domains = ["@gmail.com", "@yahoo.com",
                           "@hotmail.com", "@outlook.com"]

        if any(domain in self._email for domain in allowed_domains):
            print(f"Accessing email property...{datetime.datetime.now()}")
            return self._email
        else:
            print("Invalid email format.")
            return None

    @email.setter
    def email(self, new_email):
        allowed_domains = ["@gmail.com", "@yahoo.com",
                           "@hotmail.com", "@outlook.com"]

        if any(domain in new_email for domain in allowed_domains):
            print(f"Email is being updated...{datetime.datetime.now()}")
            self._email = new_email
        else:
            print("Invalid email format. Email not updated.")


user1 = User("password123", "user1@gmail.com", "user1")
print(user1.email)  # 1. Getter executes
user1.email = "Tejas@outlook.com"  # 2. Setter executes
print(user1.email)  # 3. Getter executes again
