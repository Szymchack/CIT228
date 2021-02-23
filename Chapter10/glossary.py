import json




def menu():
    selection= int(input("1-create file, 2-read file, 3-add to file, 4-quit"))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try it again")
    return selection

def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("Chapter10/glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append(new_word):
    with open("Chapter10/glossary.json", "r+") as add_file:
        glossary_Dictionary = json.load(add_file)
        glossary_Dictionary.update(new_word)
        add_file.seek(0)
        json.dump(glossary_Dictionary, add_file, indent=4, sort_keys=True)
        print("The new word" + new_word + "has been add to the file")

def read():
    try:
        with open ("Chapter10/glossary.json") as read_file:
            glossary_Dictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file cannot be found or does not exist")
        print("Please make a different selection")
    else:
        for key, value in glossary_Dictionary.item():
            print(key.title(), "Please enter a new term", value)

def get_key():
    word=input("Enter the new term you would like to use")
    new_word = word.split[0]
    new_word = new_word.lower()
    return new_word

def get_value():
    new_definition=str(input("Enter the definition to the new term"))
    return new_definition

glossary={
    'dictionary':'A collection of key-value pairs.',
    'key value pairs':'is an unordered collection of data values, used to store data values like a map',
    'variables':'are nothing but reserved memory locations to store values.',
    'tuple':'is one of 4 built-in data types in Python used to store collections of data which is ordered and unchangeable',
    'data types':'Since everything is an object in Python, data types are actually classes and variables are instance of these classes.',
    'del':'command used to remove a key:value pair from the dictionary',
    'key':'value used to access data stored in the dictionary or glossary',
    'conditional test':'a comparison between two values',
    'boolean':'an expression that evaluates to "true" or "false"',
    'value':'an item associated with a key in dictionary or glossary'
}

choice=menu()
while choice != 4:
    if choice == 1:
        create(new_definition)
    elif choice == 2:
        read()
    elif choice == 3:
        new_word=get_key()
        new_definition=get_value()
        new_definition_entry={new_word:new_definition}
        append(new_definition_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()