print("---------------8-3----------------")
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nYou ordered a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love love as an idea!')
make_shirt(message="Just don't.", size='x-large')

print("---------------8-4---------------")

def make_shirt(size='large', message='Can I go home now?'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='3x-large')
make_shirt('small', 'Programmers do it with class.')