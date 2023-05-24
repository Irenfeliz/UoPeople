alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# Write a function called has_duplicates that takes a string parameter and returns True if the string has any
# repeated characters. Otherwise, it should return False.

# Implement has_duplicates by creating a histogram using the histogram function above.

def has_duplicates(s):
    hist = histogram(s)
    for k, v in hist.items():
        if v > 1:
            return True
    return False


# Write a loop over the strings in the provided test_dups list. Print each string in the list and whether or not it
# has any duplicates based on the return value of has_duplicates for that string. For example, the output for "aaa"
# and "abc" would be the following.
#
# aaa has duplicates
# abc has no duplicates

print()
print('Output for test_dups and has_duplicates function:')

for s in test_dups:
    if has_duplicates(s):
        print(s, 'has duplicates')
    else:
        print(s, 'has no duplicates')


# Output for test_dups and has_duplicates function:
# zzz has duplicates
# dog has no duplicates
# bookkeeper has duplicates
# subdermatoglyphic has no duplicates
# subdermatoglyphics has duplicates

# Part 2

# Write a function called missing_letters that takes a string parameter and returns a new string with all the letters
# of the alphabet that are not in the argument string. The letters in the returned string should be in alphabetical
# order.

# Your implementation should use a histogram from the histogram function. It should also use the global variable
# alphabet. It should use this global variable directly, not through an argument or a local copy. It should loop over
# the letters in alphabet to determine which are missing from the input parameter.
#
# The function missing_letters should combine the list of missing letters into a string and return that string.

def missing_letters(s):
    lst = []
    hist = histogram(s)
    for c in alphabet:
        if c not in hist:
            lst.append(c)
    no_chars = ''.join(lst)
    return no_chars


# Write a loop over the strings in list test_miss and call missing_letters with each string. Print a line for each
# string listing the missing letters. For example, for the string "aaa", the output should be the following.
#
# aaa is missing letters bcdefghijklmnopqrstuvwxyz
#
# If the string has all the letters in alphabet, the output should say it uses all the letters. For example,
# the output for the string alphabet itself would be the following.
#
# abcdefghijklmnopqrstuvwxyz uses all the letters
#
# Print a line like one of the above for each of the strings in test_miss.

print()
print('Output for test_miss and missing_letters function:')

for s in test_miss:
    if missing_letters(s):
        print(s, 'is missing letters', missing_letters(s))
    else:
        print(s, 'uses all the letters')

# Output for test_miss and missing_letters function:
# zzz is missing letters abcdefghijklmnopqrstuvwxy
# subdermatoglyphic is missing letters fjknqvwxz
# the quick brown fox jumps over the lazy dog uses all the letters