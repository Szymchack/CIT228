def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['Chapter10/prophetic_warrior.txt', 'Chapter10/warrior.txt', 'Chapter10\prophetic.txt']
for filename in filenames:
    count_words(filename)

def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words_count = contents.lower().count(word)
        words_count = len(word)
        print(f"The file {filename} has about {words_count} {word} words.")
searchWord=input("What common word would you like to search for within the files? ")    
for filename in filenames:
    find_words(filename,searchWord)