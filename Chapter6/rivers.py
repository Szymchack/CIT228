rivers={
    'Indus':'Tibet, Kashmir, and Pakistan',
    'Rhine':'Switzerland, Germany, and The Netherlands',
    'Volga':'Russia'
}
for river, country in rivers.items():
    print("The " + river.title() + " river flows through " + country.title() + ".")

print("\n The items in the key list for rivers are:")
for river in rivers.keys():
    print("- " + river.title())

print("\n The items in the values list for countries are:")
for country in rivers.values():
    print("- " + country.title())