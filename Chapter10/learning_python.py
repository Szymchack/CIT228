print("--------------------10-1--------------------")

filename = "Chapter10/learning_python.txt"

print("---Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Lopping over the lines")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n---Storing the lines in a list (my favorite):")
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

print("--------------------10-2--------------------")

filename = "Chapter10/learning_python.txt"

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip(
        print(line.replace('Python', 'Javascript'))
    )