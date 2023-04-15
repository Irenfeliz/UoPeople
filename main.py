# Example 1. Define a function that takes an argument. Call the function.

# Identify what code is the argument and what code is the parameter.

# I'm defining the function which converts centimeters to feet and inches.

def convert_cm_to_ft(num):  # num is a parameter (it is a number in centimeters)

    ft = int(num // 30.48)  # The feet are equal to centimeters divided by 30.48

    # The inches are equal to centimeters divided by 2.54; I divide num by 2.54

    # And I subtract the entire number of feet counted in inches

    # 1 ft = 12 inches

    inch = round(num / 2.54 - 12 * ft)  # I round the number in a larger direction using the round func.

    return print(num, ' cm = ', ft, '"', inch, '\'',
                 sep='')  # My function returns conversion looks like num cm = ft"inch'


convert_cm_to_ft(180)  # 180 is an argument for my function. Here I'm calling the function with an argument 180. This
# means num = 180.

# In the output, we are getting the calculation of the function:

# 180 cm = 5"11'

# Example 2. Call your function from Example 1 three times with different kinds of arguments:

# a value, a variable, and an expression. Identify which kind of argument is which.

my_height = 172

convert_cm_to_ft(175)  # 175 is a value in the argument

convert_cm_to_ft(my_height)  # my_height is a variable in the argument

convert_cm_to_ft(1.7 * 100)  # 1.7 * 100 is an expression in the argument (here I convert meters to centimeters)

# In the output, we get proper results when passing different types of arguments to the function:

# 175 cm = 5"9'
# 172 cm = 5"8'
# 170.0 cm = 5"7'

# Example 3: Construct a function with a local variable. Show what happens when you try to use that variable outside
# the function.

# Explain the results.

# inch and ft are local variables in my function.

# ft = inch * 12
#
# # So, If I use this variable outside the function, I get an output error:
#
#     ft = inch * 12
#
#     ^^^^
#
# NameError: name 'inch' is not defined

# It happens because the variable inch exists only inside the function convert_cm_to_ft(num).

# Example 4: Construct a function that takes an argument. Give the function parameter a unique name. Show what

# happens when you try to use that parameter name outside the function. Explain the results.

# let's try to use parameter num from my function convert_cm_to_ft(num):

# meters = num / 100
#
# # Output:
#
#     meters = num / 100
#
#     ^^^
#
# NameError: name 'num' is not defined. Did you mean: 'sum'?

# I got the same issue when I used the variable “inch” outside the function.

# It is because parameters are local too. And we cannot use it outside the function.


# Example 5: Show what happens when a variable defined outside a function has the same name as a local variable
# inside a function.

# Explain what happens to the value of each variable as the program runs.

ft = my_height / 30.48  # I define a variable ft outside the function. For my program is a brand-new variable.

print(ft)  # prints the result of the expression I wrote above.

# Output:

# 5.6430446194225725

inch = my_height / 2.54  # same with variable inch. It's a new variable for my program,

# and it doesn't relate to my function convert_cm_to_ft(num).

print(inch)  # so we can calculate the expression and print the result

# Output:

# 67.71653543307086
