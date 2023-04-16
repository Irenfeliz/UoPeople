def new_line():
    print('.')


def three_lines():
    new_line()
    new_line()
    new_line()


def nine_lines():
    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    new_line()  # 1st line
    three_lines()  # + 3 lines more = 4 lines
    three_lines()  # + 3 lines more = 7 lines
    nine_lines()  # + 9 lines more = 16 lines
    nine_lines()  # + 9 lines more = 25 lines


print('Printing nine lines')  # making placeholder in the beginning
nine_lines()  # print 9 lines with "."
print('Calling clearScreen()')  # making placeholder about calling 25 lines
clear_screen()  # printing 25 lines with "."
