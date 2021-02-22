def print_magicians(unprinted_magicians, completed_magicians):
    
    while unprinted_magicians:
        current_magicians = unprinted_magicians.pop()
    
        print("Printing magician: " + current_magicians)
        completed_magicians.append(current_magicians)
        
def show_completed_magicians(completed_magicians):
    print("\nThe following magicians have been printed:")
    for completed_magicians in completed_magicians:
        print(completed_magicians)