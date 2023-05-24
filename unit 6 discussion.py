profile1 = ['Irina', 'Mikhailovna', 'Zorina']
profile2 = ['Irina', 'Mikhailovna', 'Zorina']

# These objects (lists) are equivalent because they keep equal information (values)
print(profile1 == profile2)  # Output: True

# but they are not identical, profile1 and profile2 are referred to two different objects
print(profile1 is profile2)  # Output: False

profile3 = profile2

# These objects (lists) are equivalent because they keep equal information (values)
print(profile3 == profile2)  # Output: True

# and they are identical because these variables are referred to the same object
print(profile3 is profile2)  # Output: True

# let's compare profile3 and profile1. These objects are equivalent, and they contain equal values
print(profile3 == profile1)  # Output: True

# but they are not identical because variables point to different objects
print(profile3 is profile1)  # Output: False

#

profile2 = ['Irina', 'Mikhailovna', 'Zorina']
# The variable "profile2" is a reference to the list object ['Irina', 'Mikhailovna', 'Zorina']
# The list object contains references to the strings 'Irina', 'Mikhailovna', and 'Zorina'
# Objects that pointed by variables profile1 and profile2 are two different objects

profile3 = profile2


# profile3 is a new reference to the same list object as profile2
# "profile3" and "profile2" are now aliases, which means they both refer to the same list object

#
# define the function that changes list object
def complete_profile(profile):  # takes a list 'profile' as a parameter
    age = int(input('how old are you? '))
    profile.append(age)  # add new element to the end of the list
    del profile[1]  # delete element with index 1
    country = input('where do you live? ')
    profile.append(country)  # add new element to the end of the list
    university = 'UoPeople'
    profile.insert(0, university)  # add new element (university) to the beginning of the list, index 0
    return profile  # returns updated list object


print('profile1 =', complete_profile(profile1))
# Input: how old are you? 36
# Input: where do you live? Montenegro
# Output: profile1 = ['UoPeople', 'Irina', 'Zorina', 36, 'Montenegro']


print('profile2 =', complete_profile(profile2))
# Input: how old are you? 18
# Input: where do you live? Russia
# Output: profile2 =  ['UoPeople', 'Irina', 'Zorina', 18, 'Russia']

print('profile3 =', profile3)
# Output: profile3 =  ['UoPeople', 'Irina', 'Zorina', 18, 'Russia']

numbers = [1, 5, 8, 3, 6, 7, 9, 10, 4, 5, 2, 8, 5, 7]
print(numbers.count(5))
