visited_countries = 'Austria, Spain, Portugal, Bulgaria, Czech Republic, Armenia, Finland, France, Germany, Hungary, Italy, Latvia, Monaco, Montenegro, Estonia, Russian Federation, San Marino, Thailand, Slovakia, Turkey, Brazil, Ukraine'

list_of_visited_countries = visited_countries.split(', ')
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 22 ['Austria', 'Spain', 'Portugal', 'Bulgaria', 'Czech Republic', 'Armenia', 'Finland', 'France', 'Germany', 'Hungary', 'Italy', 'Latvia', 'Monaco', 'Montenegro', 'Estonia', 'Russian Federation', 'San Marino', 'Thailand', 'Slovakia', 'Turkey', 'Brazil', 'Ukraine']


list_of_visited_countries.remove('France')
print(len(list_of_visited_countries), list_of_visited_countries)  # list without 'France'
# Output: 21 ['Austria', 'Spain', 'Portugal', 'Bulgaria', 'Czech Republic', 'Armenia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Latvia', 'Monaco', 'Montenegro', 'Estonia', 'Russian Federation', 'San Marino', 'Thailand', 'Slovakia', 'Turkey', 'Brazil', 'Ukraine']


list_of_visited_countries.pop(list_of_visited_countries.index('Russian Federation'))
print(len(list_of_visited_countries), list_of_visited_countries)  # list without 'Russian Federation'
# Output: 20 ['Austria', 'Spain', 'Portugal', 'Bulgaria', 'Czech Republic', 'Armenia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Latvia', 'Monaco', 'Montenegro', 'Estonia', 'San Marino', 'Thailand', 'Slovakia', 'Turkey', 'Brazil', 'Ukraine']


del list_of_visited_countries[12]  # list_of_visited_countries.index('Montenegro') == 12
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 19 ['Austria', 'Spain', 'Portugal', 'Bulgaria', 'Czech Republic', 'Armenia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Latvia', 'Monaco', 'Estonia', 'San Marino', 'Thailand', 'Slovakia', 'Turkey', 'Brazil', 'Ukraine']


list_of_visited_countries.sort()
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 19 ['Armenia', 'Austria', 'Brazil', 'Bulgaria', 'Czech Republic', 'Estonia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Latvia', 'Monaco', 'Portugal', 'San Marino', 'Slovakia', 'Spain', 'Thailand', 'Turkey', 'Ukraine']


list_of_visited_countries.insert(10, 'Serbia')
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 20 ['Armenia', 'Austria', 'Brazil', 'Bulgaria', 'Czech Republic', 'Estonia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Serbia', 'Latvia', 'Monaco', 'Portugal', 'San Marino', 'Slovakia', 'Spain', 'Thailand', 'Turkey', 'Ukraine']


list_of_visited_countries.append('Bosnia and Herzegovina')
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 21 ['Armenia', 'Austria', 'Brazil', 'Bulgaria', 'Czech Republic', 'Estonia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Serbia', 'Latvia', 'Monaco', 'Portugal', 'San Marino', 'Slovakia', 'Spain', 'Thailand', 'Turkey', 'Ukraine', 'Bosnia and Herzegovina']


new_visit_countries = ['Albania', 'Croatia']
list_of_visited_countries.extend(new_visit_countries)
print(len(list_of_visited_countries), list_of_visited_countries)
# Output: 23 ['Armenia', 'Austria', 'Brazil', 'Bulgaria', 'Czech Republic', 'Estonia', 'Finland', 'Germany', 'Hungary', 'Italy', 'Serbia', 'Latvia', 'Monaco', 'Portugal', 'San Marino', 'Slovakia', 'Spain', 'Thailand', 'Turkey', 'Ukraine', 'Bosnia and Herzegovina', 'Albania', 'Croatia']

all_visited_countries = ', '.join(list_of_visited_countries)
print(all_visited_countries)
# Output: Armenia, Austria, Brazil, Bulgaria, Czech Republic, Estonia, Finland, Germany, Hungary, Italy, Serbia, Latvia, Monaco, Portugal, San Marino, Slovakia, Spain, Thailand, Turkey, Ukraine, Bosnia and Herzegovina, Albania, Croatia


# [[Grandparents [father's side], [mother's side]] - [Parents] - [Kids] - [Grandchildren]]
family = [[['Leonid', 'Maria'], ['Nikolay', 'Irma']], ['Mikhail', 'Natalya'], ['Irina', 'Olga'], ['Alexander', 'Grigory']]
print(family)
# Output: [[['Leonid', 'Maria'], ['Nikolay', 'Irma']], ['Mikhail', 'Natalya'], ['Irina', 'Olga'], ['Alexander', 'Grigory']]
print(family[0][1][1])  # My grandmother from father's side
# Output: Irma
print(family[2][0])  # It's me
# Output: Irina

monday_schedule = ['algebra', 'history', 'art', 'english']
week_schedule = monday_schedule * 5
print(week_schedule)
# Output: ['algebra', 'history', 'art', 'english', 'algebra', 'history', 'art', 'english', 'algebra', 'history', 'art', 'english', 'algebra', 'history', 'art', 'english', 'algebra', 'history', 'art', 'english']

print(week_schedule[4:8])
# Output: ['algebra', 'history', 'art', 'english']

monday_schedule[1:3] = ['math']
print(monday_schedule)
# Output: ['algebra', 'math', 'english']

week_schedule[5:10] = monday_schedule
print(week_schedule)
# Output: ['algebra', 'history', 'art', 'english', 'algebra', 'algebra', 'math', 'english', 'art', 'english', 'algebra', 'history', 'art', 'english', 'algebra', 'history', 'art', 'english']

grocery_list = ['potato', 'milk', 'butter']
carbonara_ingredients = ['spaghetti', 'bacon', 'olive oil', 'eggs', 'pecorino', 'parmesan', 'salt', 'black pepper']
grocery_list += carbonara_ingredients
print(grocery_list)
# output: ['potato', 'milk', 'butter', 'spaghetti', 'bacon', 'olive oil', 'eggs', 'pecorino', 'parmesan', 'salt', 'black pepper']

def grocery_count():
        grocery_list = ['potato', 'milk', 'butter']
        carbonara_ingredients = ['spaghetti', 'bacon', 'olive oil', 'eggs', 'pecorino', 'parmesan', 'salt',
                                 'black pepper']
        total = len(grocery_list)
        for i in carbonara_ingredients:
                total += 1
                grocery_list += [i]
        return total, grocery_list

print(grocery_count())
# Output: (11, ['potato', 'milk', 'butter', 'spaghetti', 'bacon', 'olive oil', 'eggs', 'pecorino', 'parmesan', 'salt', 'black pepper'])

def only_words(text):
    new_text = []  # creating new list object
    for s in text:  # checking every item in the list
        if s == str(s):  # we need to check only strings
            if s.isalpha():  # checking if all the characters in the string are letters
                new_text.append(s)  # if yes, adding this string to the new list
    return print(new_text)


song = ['Jingle', 5.605, 'bells', 1231, 'jingle', 'bells', 'Jingle', 2023, 'all', 'the', 'way', '^%$%', 'Oh', 'what',
        'fun', 'it', '!)(@#$%', 'is', 'to', 'ride', 12312022, 'In', 'a', 'one', 'horse', 'open', '     ', 'sleigh',
        'hey']
only_words(song)
# Output: ['Jingle', 'bells', 'jingle', 'bells', 'Jingle', 'all', 'the', 'way', 'Oh', 'what', 'fun', 'it', 'is', 'to', 'ride', 'In', 'a', 'one', 'horse', 'open', 'sleigh', 'hey']


