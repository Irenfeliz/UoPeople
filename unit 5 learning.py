prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in 'OQ':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# Output:
# Jack
# Kack
# Lack
# Mack
# Nack
# Ouack
# Pack
# Quack

# Part2
# For my example I'll use the date format: 'dd.mm.yyyy hh.mm.ss'. I'll slice the date into 2 parts: day and time.
# It might be useful when we need to parse a file.
print(len('dd.mm.yyyy hh.mm.ss'))  # checking how many symbols contains the string


# Output: 19
# 19 characters, so we use indexes from 0 to 18

def only_day(date):  # define the function that returns the date in format 'dd.mm.yyyy'
    return date[:10]  # it returns the first 10 characters from the string, indexes are 0-9, index 10 - space


print(only_day('19.09.1986 09.15.45'))
print(only_day('23.02.2003 10.00.30'))


# Output: 19.09.1986
# Output: 23.02.2003

def only_time(date):  # define the function that returns the time in format hh.mm.ss
    return date[11:]  # it returns all characters from 12 till, indexes are 11 - 18


print(only_time('19.09.1986 09.15.45'))
print(only_time('23.02.2003 22.00.30'))
print(only_time('05.04.2000 17.00.30'))


# Output: 09.15.45
# Output: 22.00.30
# Output: 17.00.30


def date_in_12h_format(date):  # let's make the date in 12-hour time format
    if int(date[11:13]) > 12:  # I take 'hh' from the date and turn it to the integer, then compare with 12
        hh = int(date[11:13]) - 12  # if it bigger than 12, I subtract 12 from hh
        return date[:11] + str(hh) + date[13:] + ' PM'  # The function has to return string,
        # so I turn integer hh back to string
    elif date[11:13] == '12':  # if 'hh' = '12' I pass PM to the date
        return date + ' PM'
    elif date[11:13] == '00':  # if 'hh' = '00' , I change it to 12 and pass AM to the date
        return date[:11] + '12' + date[13:] + ' AM'
    else:
        return date + ' AM'  # in other cases it's AM time


print(date_in_12h_format('19.09.1986 09.15.45'))
print(date_in_12h_format('23.02.2003 22.00.30'))
print(date_in_12h_format('05.04.2000 17.00.30'))
print(date_in_12h_format('10.07.2019 00.00.30'))
print(date_in_12h_format('01.10.1895 12.00.30'))


# Output: 19.09.1986 09.15.45 AM
# Output: 23.02.2003 10.00.30 PM
# Output: 05.04.2000 5.00.30 PM
# Output: 10.07.2019 12.00.30 AM
# Output: 01.10.1895 12.00.30 PM

def month_in_word(date):  # define the function that changes month number to its word.
    if date[3:5] == '01':  # check the characters with indexes 3 and 4 that use for 'mm' in the string
        return date[:2] + ' January ' + date[6:]  # take the first 2 characters with indexes 0-1
        # 'dd' + word + 'yyyy' with indexes 6-9
    elif date[3:5] == '02':
        return date[:2] + ' February ' + date[6:]
    elif date[3:5] == '03':
        return date[:2] + ' March ' + date[6:]
    elif date[3:5] == '04':
        return date[:2] + ' April ' + date[6:]
    elif date[3:5] == '05':
        return date[:2] + ' May ' + date[6:]
    elif date[3:5] == '06':
        return date[:2] + ' June ' + date[6:]
    elif date[3:5] == '07':
        return date[:2] + ' July ' + date[6:]
    elif date[3:5] == '08':
        return date[:2] + ' August ' + date[6:]
    elif date[3:5] == '09':
        return date[:2] + ' September ' + date[6:]
    elif date[3:5] == '10':
        return date[:2] + ' October ' + date[6:]
    elif date[3:5] == '11':
        return date[:2] + ' November ' + date[6:]
    else:
        return date[:2] + ' December ' + date[6:]


print(month_in_word('19.09.1986'))
print(month_in_word('01.01.2001'))
print(month_in_word('03.12.2023'))


# Output:
# 19 September 1986
# 01 January 2001
# 03 December 2023

# and as a bonus task, let's use two functions for formatting the date to 12h and word instead of month's number
def month_in_word_and_12h_format(date):
    new_date = date_in_12h_format(date)
    return month_in_word(new_date)


print(month_in_word_and_12h_format('19.09.1986 09.15.45'))
print(month_in_word_and_12h_format('23.02.2003 22.00.30'))
print(month_in_word_and_12h_format('05.04.2000 17.00.30'))
print(month_in_word_and_12h_format('10.07.2019 00.00.30'))
print(month_in_word_and_12h_format('01.10.1895 12.00.30'))

# Outputs:
# 19 September 1986 09.15.45 AM
# 23 February 2003 10.00.30 PM
# 05 April 2000 5.00.30 PM
# 10 July 2019 12.00.30 AM
# 01 October 1895 12.00.30 PM
