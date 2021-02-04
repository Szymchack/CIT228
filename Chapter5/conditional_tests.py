movie='True Women'
print("Is movie == 'True Women'? I predict True.")
print(movie == 'True Women')

print("\nIs movie == 'True Grit'? I predict False.")
print(movie == 'True Grit')
print("---------------------------------------------")
bus_drivers = ['cathyann', 'kyle', 'sid']
driver='kyle'
for driver in bus_drivers:
    if driver == 'kyle':
        print(driver.upper())
    else:
        print(driver.title())
print("---------------------------------------------")
driver ='kyle'
for driver in bus_drivers:
    if driver == 'kyle':
        print("'kyle'True-I predict true!")
    else:
        print("\nFalse, you cannot drive this unit.")
print("---------------------------------------------")
pizza='Pickle Pizza'
print("Does pizza == 'Pickle Pizza'? I predict True")
print(pizza == 'Pickle Pizza')
print("\nDoes pizza == 'pickle Pizza'? I predict False due to case.")
print(pizza == 'pickle Pizza')
print("---------------------------------------------")
age_0 = 45
age_1 = 50

if age_0 >= 49 or age_1 >= 49:
    print("age_0 >= 49 or age_1 >= 49:This statement is true, which I predicted.")
else:
    print("This statement is false.")
print("------------------------------------------------")
if age_0 >= 66 or age_1 >= 66:
    print("This statement is true!")
else:
    print("age_0 >= 66 or age_1 >= 66:This statement is false, which I predicted!")
print("------------------------------------------------")

requested_driver = ['sub', 'alternate', 'lead']
if 'sub' in requested_driver:
    print("Sub in requested driver is True, predicted answer")
else:
    print("False")

if 'mechanic' in requested_driver:
    print("True")
else:
    print("False, I suggest using a driver for this trip not a mechanic.")

print("--------------------5-2---------------------------")

age = 25
if age >21:
    print("True, you are of legal age to drink")
if age == 21:
    print("great")
else:
    print("This is a false statement.")




