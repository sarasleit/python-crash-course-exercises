class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1 
    def describe_user(self):
        print(f"The user name is: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome.")
    def rest_login_attempts(self):
        self.login_attempts = 0

user1 = User("Sara", "Sleit")
user2 = User("Noor", "Sleit")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.rest_login_attempts()
print(f"{user1.login_attempts}")

