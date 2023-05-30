countries = ['France', 'Spain', 'Montenegro', 'Hungary', 'Serbia', 'Bosnia and Hercegovina']
cities = [['Nice', 'Paris', 'Lyon', 'Bordeaux'], ['Barcelona', 'Madrid', 'Granada', 'Tarifa', 'Sevilla'], ['Budva', 'Podgorica', 'Kotor', 'Zabljak', 'Herceg Novi'], ['Budapest'], ['Beograd', 'Novi Sad'], ['Mostar', 'Sarajevo']]

my_dict = dict(zip(countries, cities))
print('My dictionary before inversion:', my_dict, sep='\n')

# Output:
# My dictionary before inversion:
# {'France': ['Nice', 'Paris', 'Lyon', 'Bordeaux'], 'Spain': ['Barcelona', 'Madrid', 'Granada', 'Tarifa', 'Sevilla'], 'Montenegro': ['Budva', 'Podgorica', 'Kotor', 'Zabljak', 'Herceg Novi'], 'Hungary': ['Budapest'], 'Serbia': ['Beograd', 'Novi Sad'], 'Bosnia and Hercegovina': ['Mostar', 'Sarajevo']}

def invert_dict(d):
    inverse = dict()
    for key, val in d.items():  # checking key-value pairs from dictionary
        for s in val:  # taking every element from each lists in values
            if s not in inverse:
                inverse[s] = [key]  # inverting string to the key and key to the value
            else:
                inverse[s].append(key) # if there is a key exists already in new dictionary, I add the new value to the list
    return inverse

print('My dictionary after inversion:', invert_dict(my_dict), sep='\n')

# Output:
# My dictionary after inversion:
# {'Nice': ['France'], 'Paris': ['France'], 'Lyon': ['France'], 'Bordeaux': ['France'], 'Barcelona': ['Spain'], 'Madrid': ['Spain'], 'Granada': ['Spain'], 'Tarifa': ['Spain'], 'Sevilla': ['Spain'], 'Budva': ['Montenegro'], 'Podgorica': ['Montenegro'], 'Kotor': ['Montenegro'], 'Zabljak': ['Montenegro'], 'Herceg Novi': ['Montenegro'], 'Budapest': ['Hungary'], 'Beograd': ['Serbia'], 'Novi Sad': ['Serbia'], 'Mostar': ['Bosnia and Hercegovina'], 'Sarajevo': ['Bosnia and Hercegovina']}

future_travel = {'USA': ['New York', 'Los Angeles', 'Saint Petersurg'], 'Russia': ['Moscow', 'Saint Petersurg', 'Ekaterinburg']}

print(invert_dict(future_travel))
# Output:
# {'New York': ['USA'], 'Los Angeles': ['USA'], 'Saint Petersurg': ['USA', 'Russia'], 'Moscow': ['Russia'], 'Ekaterinburg': ['Russia']}
