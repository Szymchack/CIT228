number = input("Give me a number and I will tell you if it is a multiple of 10:")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10, Yee Haa!")
else:
    print(str(number) + " is not a multiple of 10, too bad.")