party=input("How many people are there in your party, please?")
party=int(party)
if party > 8:
    print(f"\n I am sorry, you will have to wait until a table is ready")
else:
    print(f"\nYour table is ready!")