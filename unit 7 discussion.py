countries = ['Austria', 'Spain', 'Portugal', 'Bulgaria', 'The Czech Republic', 'Armenia', 'Finland', 'France']

for i, country in enumerate(countries): # the enumerate() function returns tuples containing the index and the corresponding element of the list.
    print('The country number',i + 1, 'I visited was', country)

# The country number 1 I visited was Austria
# The country number 2 I visited was Spain
# The country number 3 I visited was Portugal
# The country number 4 I visited was Bulgaria
# The country number 5 I visited was The Czech Republic
# The country number 6 I visited was Armenia
# The country number 7 I visited was Finland
# The country number 8 I visited was France

# Making a list of capitals of those countries
capitals = ['Vienna', 'Madrid', 'Lisbon', 'Sofia', 'Prague', 'Yerevan', 'Helsinki', 'Paris']

for pair in zip(countries, capitals):
    print(pair)

# Output:
# ('Austria', 'Vienna')
# ('Spain', 'Madrid')
# ('Portugal', 'Lisbon')
# ('Bulgaria', 'Sofia')
# ('The Czech Republic', 'Prague')
# ('Armenia', 'Yerevan')
# ('Finland', 'Helsinki')
# ('France', 'Paris')

country_capital = dict(zip(countries, capitals))  # creating dictionary using built-in function zip()
print(country_capital)
# {'Austria': 'Vienna', 'Spain': 'Madrid', 'Portugal': 'Lisbon', 'Bulgaria': 'Sofia', 'The Czech Republic': 'Prague',
# 'Armenia': 'Yerevan', 'Finland': 'Helsinki', 'France': 'Paris'}

print(country_capital.items())
# Output: dict_items([('Austria', 'Vienna'), ('Spain', 'Madrid'), ('Portugal', 'Lisbon'), ('Bulgaria', 'Sofia'),
# ('The Czech Republic', 'Prague'), ('Armenia', 'Yerevan'), ('Finland', 'Helsinki'), ('France', 'Paris')])


for country, capital in country_capital.items():  #  the items() method of the dictionary returns tuples containing the key-value pairs
    print(country, '-', capital)

# Output:
# Austria - Vienna
# Spain - Madrid
# Portugal - Lisbon
# Bulgaria - Sofia
# The Czech Republic - Prague
# Armenia - Yerevan
# Finland - Helsinki
# France - Paris


