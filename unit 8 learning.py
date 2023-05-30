file = open('dict.txt', encoding='utf-8') # open file in read mode
def make_dict_from_file(file): # creating new function
    my_dict = {} # creating empty dictionary
    for line in file: # taking line
        key = line[:line.find(':')] # name of the country locates before ':' symbol, so I found the index of ':' and
        # make a slice of string from beginning (index 0) till ':' symbol.
        value = (line[line.find(':') + 2:].strip()).split(', ') # cities locate after ':' symbol. So
        # I pass elements after ':' to the value. And split string to list.
        my_dict[key] = value # add data to the dictionary
    return my_dict

my_dict = make_dict_from_file(file)
print('My dictionary before inversion:', my_dict, sep='\n')

# Output:
# My dictionary before inversion:
# {'France': '[Nice, Paris, Lyon, Bordeaux]', 'Spain': '[Barcelona, Madrid, Granada, Tarifa, Sevilla]', 'Montenegro': '[Budva, Podgorica, Kotor, Zabljak, Herceg Novi]', 'Hungary': '[Budapest]', 'Serbia': '[Beograd, Novi Sad]', 'Bosnia and Hercegovina': '[Mostar, Sarajevo]'}

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

file_new = open('dict_new.txt', 'w', encoding='utf-8') # creating new txt file with writing access
for key, value in invert_dict(my_dict).items(): # taking data (key and value) from dictionary one by one with for loop
    new_line = str(key) + ': ' + str(*value) # creating the string of those data
    file_new.write(new_line + '\n') # writing this string to the file


