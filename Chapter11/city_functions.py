print("---------------11-1---------------")

def city_country(city, country):
  
    return f"{city.title()}, {country.title()}"

print("---------------11-2---------------")   

def city_country(city, country, population):
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string

def city_country(city, country, population=0):
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string