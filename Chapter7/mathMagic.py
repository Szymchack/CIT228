import random
problems = int(input("How many math problems would you like to practice?"))
counter=0
numberCorrect=0
while counter < problems:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer==yourAnswer:
        print("Great scott, you did it!")
        numberCorrect +=1
    else:
        print("Well, better luck next time!")
        counter +=1

print("You answered ", numberCorrect, "question correctly!")
print("Thanks for playing!")
