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

#commit_2
# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

# Print the average temperature of all the cities
print('The average temperature of all the cities:')
temp_all = list(map(lambda x: float(x['temperature']), cities))
print(sum(temp_all)/len(temp_all))
print()

# Print all cities in Germany
print('All cities in Germany: ')
germany = filter(lambda x: x['country'] == 'Germany', cities) 
for city_name in (list(map(lambda c: c['city'], germany))):
    print(city_name)
print()

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    data = []
    for item in dict_list:
        x = item[aggregation_key]
        try:
            x = float(x)
        except ValueError:
            pass
        data.append(x)
    return aggregation_function(data)

# Print all cities in Spain with a temperature above 12°C
print('All cities in Spain with a temperature above 12°C:')
spain_filter_12 = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
for spain_city_name in (list(map(lambda x: x['city'], spain_filter_12))):
    print(spain_city_name)
print()

# Count the number of unique countries
print('The number of unique countries:')
country_uniq = []
list(map(lambda c: country_uniq.append(c['country']) 
        if c['country'] not in country_uniq else None, cities))
print(len(country_uniq))
print()

# Print the average temperature for all the cities in Germany
print('the average temperature for all the cities in Germany: ')
german_filtered = filter(lambda x: x['country'] == 'Germany', cities)
german_temp = aggregate('temperature', lambda x: sum(x)/len(x), german_filtered)
print(german_temp)
print()

# Print the max temperature for all the cities in Italy
print('The max temperature for all the cities in Italy:')
italy_filtered = filter(lambda x: x['country'] == 'Italy', cities)
italy_temp = list(map(lambda x: float(x['temperature']), italy_filtered))
print(max(italy_temp))


