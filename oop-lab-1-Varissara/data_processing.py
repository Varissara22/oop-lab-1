import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
germany_cities = []
for city in cities:
    if city['country'] == 'Germany':
        germany_cities.append(city['city'])
    else:
        continue
for germany_city in germany_cities:
    print(f"{germany_city}")
print()

# Print all cities in Spain with a temperature above 12°C
print('All cities in Spain with a temperature above 12°C:')
spain_city_above_12 = []
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        spain_city_above_12.append(city['city'])
    else:
        continue
for spaincity in spain_city_above_12:
    print(f"{spaincity}")
print()

# Count the number of unique countries
print('The number of unique countries:')
countries = []
for city in cities:
    if city['country'] in countries:
        continue
    else:
        countries.append(city['country'])
print(f"{len(countries)}")
print()

# Print the average temperature for all the cities in Germany
print('The average temperature for all the cities in Germany:')
germany_cities_temp = []
for city in cities:
    if city['country'] == 'Germany':
        germany_cities_temp.append(float(city['temperature']))
    else:
        continue
print(f"{(sum(germany_cities_temp)/len(germany_cities_temp))}")
print()

# Print the max temperature for all the cities in Italy
print('The max temperature for all the cities in Italy:')
italy_cities_temp = []
for city in cities:
    if city['country'] == 'Italy':
        italy_cities_temp.append(float(city['temperature']))
    else:
        continue
print(f"{max(italy_cities_temp)}")
print()




