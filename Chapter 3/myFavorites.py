foods=["Pot Roast", "Chaffels", "Chimichanga", "Chili Cheese Fries", "Bacon", "Barbeque"]
print(f"Favorite food:{foods[0], foods[1], foods[2], foods[3], foods[4], foods[5]}")

numbers=["8", "88", "10", "5", "23", "3"]
print(f"Favorite number:{numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]}")

movies=["Harry Potter", "Die Hard", "Transformers"]
print(f"Favorite movie:{movies[0], movies[1], movies[2]}")

print(f"My combo list: {foods[0]}, {foods[-1]}, {numbers[0]}, {numbers[1]}, {movies[0]}, {movies[1]}")

print(f"Last food item: {foods[-1]}")

print(f"2nd, 4th, and 6th number: {numbers[1]}, {numbers[3]}, {numbers[-1]}")

print(f"All Movies: {movies[0]}, {movies[1]}, {movies[2]}")

print(f"First food, First number, First movie: {foods[0]}, {numbers[0]}, {movies[0]}")

movies.append('Calamity Jane')
print(movies)

numbers.insert(3, '25')
print(numbers)

foods.insert(5, 'Cream Cheese')
print(foods)

del foods[5]
print(foods)

popped_numbers=numbers.pop()
print(numbers)
print(popped_numbers)

popped_2=numbers.pop(2)
print(numbers)
print(popped_2)

print("Here is the Original List:" )
print((movies))
print("/nHere is the Sorted List:")
print(sorted(movies))

print("Here is the Sorted List of foods:")
print(sorted(foods))

print("Here is the Original List:" )
print((numbers))
print("\nHere is the Sorted List:")
print(sorted(numbers))
print("\nHere is the Original List Again:")
print(numbers)

print(movies)
movies.reverse()
print(movies)
