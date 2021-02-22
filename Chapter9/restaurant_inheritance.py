print("--------------------9-6---------------------")

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

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type = 'ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors=[]

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

black_opal = Restaurant('the black opal', 'seafood')
black_opal.describe_restaurant()

maestro = Restaurant("maestro's", 'italian')
maestro.describe_restaurant()

mimi = Restaurant("mimi's", 'home cooking')
mimi.describe_restaurant()

cats_cream = IceCreamStand('Cats Cream Ice Cream')
cats_cream.flavors = ['blue moon', 'vanilla', 'chocolate', 'cheesecake'] 
cats_cream.describe_restaurant()
cats_cream.show_flavors()


