print("--------------------9-1---------------------")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves the freshest " + self.cuisine_type + " around!"
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open, come as you are and bring your friends!"
        print("\n" + msg)

restaurant = Restaurant('the black opal', 'seafood')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("--------------------9-2---------------------")

black_opal = Restaurant('the black opal', 'seafood')
black_opal.describe_restaurant()

maestro = Restaurant("maestro's", 'italian')
maestro.describe_restaurant()

mimi = Restaurant("mimi's", 'home cooking')
mimi.describe_restaurant()