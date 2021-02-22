print("--------------------9-1---------------------")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves the freshest " + self.cuisine_type + " around!"
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open, come as you are and bring your friends!"
        print("\n" + msg)

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served +=additional_served



print("--------------------9-2---------------------")

black_opal = Restaurant('the black opal', 'seafood')
black_opal.describe_restaurant()

maestro = Restaurant("maestro's", 'italian')
maestro.describe_restaurant()

mimi = Restaurant("mimi's", 'home cooking')
mimi.describe_restaurant()

print("Below printed by setting attribute")
Restaurant.number_served = 56
print("Below printed by method")
Restaurant.set_number_served = 14
print("Below is printed with increment method")
Restaurant.increment_number_served = 200 

restaurant = Restaurant('the black opal', 'seafood')