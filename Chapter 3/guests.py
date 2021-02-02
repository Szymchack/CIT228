

guests=["Dad", "Jennie", "God"]
print(f"{guests[0]} can you make it to dinner this Sunday?")
print(f"{guests[1]} can you make it to dinner this Sunday?")
print(f"{guests[2]} can you make it to dinner this Sunday?")

popped_guests=guests.pop()
print(guests)
print(popped_guests)
guests.insert(2, "Grandma Lelia")

print(f"{popped_guests} cannot make it this Sunday?")
print(f"{guests[0]} can you make it this Sunday?")
print(f"{guests[1]} can you make it this Sunday?")
print(f"{guests[2]} can you make it this Sunday?")

print(f"Awesomeness, I found a bigger dinner table")
x=len(guests)
print(x)
guests.insert(0, 'Reba McEntire')
guests.insert(2, 'Peanut')
guests.append('Kelli')
print(guests)

print(f"{guests[0]} can you make it to dinner this Sunday? ")
print(f"{guests[1]} can you make it to dinner this Sunday? ")
print(f"{guests[2]} can you make it to dinner this Sunday? ")
print(f"{guests[3]} can you make it to dinner this Sunday? ")
print(f"{guests[4]} can you make it to dinner this Sunday? ")
print(f"{guests[5]} can you make it to dinner this Sunday? ")



print(f"My table will not arrive by Sunday so I can only invite two people")
last_guests = guests.pop()
print(f"Sorry {last_guests.title()} I cannot invite you for Sunday.")
next_guests = guests.pop()
print(f"Sorry {next_guests.title()} I cannot invite you for Sunday.")
another_guests = guests.pop(0)
print(f"Sorry {another_guests.title()} I cannot invite you for Sunday.")
finish_guest=guests.pop(1)
print(f"Sorry {finish_guest.title()} I cannot invite you for Sunday.")

print(f"{guests[0]} can you make it to dinner this Sunday?")
print(f"{guests[1]} can you make it to dinner this Sunday?")

del guests[0]
del guests[0]
print(f"This is my number of guests now:{guests}")




