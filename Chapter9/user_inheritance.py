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

class Privileges():

    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges")

class Admin(User):

    def __init__(self, first_name, last_name, email, username, location, password):
        super().__init__(first_name, last_name, email, username, location, password)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")

cathyann = Admin('cathyann', 'szymchack', 'c_szymchack@example.com', 'cat', 'the beach', 'really')
cathyann.describe_user()

cathyann.privileges.show_privileges()

print("\nAdding privileges...")
cathyann_privileges = [
    'can reset passwords',
    'can mediate discussions',
    'can boot you outta account'
]

cathyann.privileges.privileges = cathyann_privileges
cathyann.privileges.show_privileges()



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