import datetime


class User:
    def __init__(self, password, email, username):
        self.password = password
        self._email = email
        self.username = username

    def say_hi_to_user(self, user):
        print(
            f"Hello, {user.username}! My username is {self.username} and email is {self.email}.")

    def get_email(self):  # getter method for email
        return self._email

    def set_email(self, new_email):  # setter method for email
        print(f"Email is being updated...{datetime.datetime.now()}")
        if "@gmail.com" or "@yahoo.com" or "@hotmail.com" or "@outlook.com" in new_email:
            self._email = new_email


user1 = User("password123", "user1@example.com", "user1")
print(user1.get_email())

user1.set_email("daefefe@outlook.com")
# shouldn't access outside the class directly, use getter and setter methods instead
print(user1.get_email())
