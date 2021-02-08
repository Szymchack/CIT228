import Chapter8.message_activity


print("--------------------8-9--------------------")
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magicians = ['david copperfield', 'criss angel', 'Cyril Takayama']

show_magicians(magicians)

print("--------------------8-10-------------------")

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['david copperfield', 'criss angel', 'cyril takayama']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

print("--------------------8-11-------------------")

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['david copperfield', 'criss angel', 'cyril takayama']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)