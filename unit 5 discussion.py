# 1

def any_lowercase1(s):
    for c in s:  # it takes the first character from the string
        if c.islower():  # checks if the character is lowercase
            return True  # if yes - function returns boolean value True and ends its work.
        else:
            return False  # if no - function returns boolean value False and ends its work.


print('lowercase1 function:')
print(any_lowercase1("Hello UoPeople!"))  # "H" is uppercase, so results is False
print(any_lowercase1("hello uopeople!"))  # "h" is lowercase, so results is True
print()  # empty string


# Output: False
# Output: True

# 2

def any_lowercase2(s):
    for c in s:  # it takes the first character from the string, but it's never used in this function
        if 'c'.islower():  # it takes lowercase letter 'c' and check if it's lowercase.
            return 'True'  # it returns string 'True' , because 'c' is lowercase (see output) and ends its work
        else:
            return 'False'  # it's never used in this function


print('lowercase2 function:')
print(any_lowercase2("Ciao UoPeople!"))
print(any_lowercase2("ciao uopeople!"))
print()  # empty string


# Output: True
# Output: True

# 3

def any_lowercase3(s):
    for c in s:  # it takes characters one by one from the string s
        flag = c.islower()  # flag = True or False, depends on the character in the string
    return flag  # return bulean value True if the last character is lowercase,
    # and False if it's uppercase or another symbol.


print('lowercase3 function:')
print(any_lowercase3("Hello UoPeople!"))  # the last character is '!' , so flag == False, the function returns False
print(any_lowercase3("hello uopeople"))  # the last character is 'e', so flag == True, the function returns True
print()  # empty string


# Output: False
# Output: True

# 4

def any_lowercase4(s):
    flag = False  # set variable 'flag' False value
    for c in s:  # it takes characters one by one from the string s
        flag = flag or c.islower()  # Flag == False or False (=False) if the character is not lowercase,
        # Flag == False or True (=True) if the character is lowercase.
        # since the function meets the lowercase character, the flag is always True.
    return flag  # returns True if the string contains a lowercase letter
    # returns False if the string doesn't contain a lowercase letter


print('lowercase4 function:')
print(any_lowercase4("Hello UoPeople!"))  # since the character 'e' in the 'Hello' flag == True
print(any_lowercase4("hello uopeoplE!"))  # since the character 'h' in the 'hello' flag == True
print(any_lowercase4("HELLO UOPEOPLE"))  # there are no on lowercase latter, so flag == False
print()  # empty string


# Output: True
# Output: True
# Output: False

# 5

def any_lowercase5(s):
    for c in s:  # it takes characters one by one from the string s
        if not c.islower():  # checking if the character is not lowercase returns not True = False
            return False  # returns boolean value False and end its iteration
    return True  # if EVERY symbol in the string is lowercase character, the function returns True.


print('lowercase5 function:')
print(any_lowercase5("Hello UoPeople!"))  # function checked the first character 'H' only and ended iteration with False result.
print(any_lowercase5("hello"))  # the function checked every character and returned True due every character is lowercase.

# Output: False
# Output: True
