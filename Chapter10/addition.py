print("---------------10-6---------------")
try:
    x = input("Give me your first number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Come on, you know that is not a number, try again.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")

print("---------------10-7---------------")

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me your first number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me your second number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Moron, that is not a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")