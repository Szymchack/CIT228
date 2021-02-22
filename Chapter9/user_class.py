class User():
    def __init__ (self, first_name, last_name, email, username, location, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.title()
        self.username = username.title()
        self.location = location.title()
        self.password = password.title()
        self.login_attempts = 0
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Email: " + self.email)
        print("  Username: " + self.username)
        print("  Location: " + self.location)
        print("  Password: " + self.password)
    
    def greet_user(self):
        print("\nWelcome back, " + self.first_name + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

lelia = User('lelia', 'borgen', 'leelee@borg.com', 'lab61820', 'Micronesia', 'rujoking')
lelia.describe_user()
lelia.greet_user()

kelli = User('kelli', 'borgen', 'bear@borg.com', 'angelbaby1', 'neitherlands', 'ecktoo')
kelli.describe_user()
kelli.greet_user()

cain = User('cain', 'szymchack', 'monkey@borg.com', 'myBoy', 'michigan', 'monkey')
cain.describe_user()
cain.greet_user()

print("--------------------9-5--------------------")

cain.increment_login_attempts()
cain.increment_login_attempts()
cain.increment_login_attempts()
print("Your number of login attempst: " + str(cain.login_attempts))
cain.reset_login_attempts()
print("We are resetting login attempts: " + str(cain.login_attempts))