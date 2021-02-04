myAnimals=["Horse", "Pig", "Alpaca", "Buffalo"]
newAnimals=myAnimals[:]
newAnimals.append("Highland Cow")
newAnimals.append("Donkey")
newAnimals.append("Belgian Horse")
newAnimals.append("African Tree Frog")
newAnimals.append("Dragon")
newAnimals.sort()
myAnimals.sort()
print("My original animals are:")
print("---------------------------------------")
for animal in myAnimals:
    print(animal)
print("---------------------------------------")
print("Then I added more and now I have:")
for animal in newAnimals:
    print(animal)
print("The first 3 animals in the new list are:", newAnimals[0:3])
print("The middle 3 animals are:", newAnimals[3:6])
print("The last 3 animals are:", newAnimals[6:10])
