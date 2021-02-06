sandwich_orders = ['tuna', 'asiago turkey club', 'vegitarian italian', 'philly cheese steak']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("\nThe following sandwiches were made today:")
    print(sandwich)

sandwich_orders = [
    'peanut butter', 'tuna', 'asiago turkey', 'peanut butter',
    'vegitarrian italian', 'philly cheese steak', 'peanut butter']
finished_sandwiches = []

print("I'm sorry, we're all out of peanut butter today.")
while 'peanut butter' in sandwich_orders:
    sandwich_orders.remove('peanut butter')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")