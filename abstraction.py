class EmailService:

    def conncect(self):
        print("Connecting to email server...")

    def authenticate(self):
        print("Authenticating user...")

    def send_email(self, recipient, subject, body):
        self.conncect()
        self.authenticate()
        print(
            f"Sending email to {recipient} with subject '{subject}' and body '{body}'")
        self.disconnect()

    def disconnect(self):
        print("Disconnecting from email server...")


user1 = EmailService()
user1.send_email("john@example.com", "Hello", "This is a test email.")
