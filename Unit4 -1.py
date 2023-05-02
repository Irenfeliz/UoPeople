# # Let’s declare the function hypotenuse with two parameters, leg1 and leg2:
#
#
# def hypotenuse(leg1, leg2):
#     return 0
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))
#
#
# # output: The length of the hypotenuse is 0
#
#
# # It is syntactically correct and returns the value (zero), but not that value we need.
#
#
# # Now let's find the sum of the squares of the lengths of the legs:
#
#
# def hypotenuse(leg1, leg2):
#     sum_squares_legs = leg1 ** 2 + leg2 ** 2
#     return sum_squares_legs
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))
#
# # The output: The length of the hypotenuse is 125
#
#
# # In the output is the result of calculating the sum of the squares. But it is not an answer to the task.
#
#
# # So now we need to extract a square from the sum_squares_legs to find the length of the hypotenuse
#
#
# # For extraction of a square, I'll use the math module, so I should import it
import math


#
#
# # Creating a new local variable len_hypotenuse and using the sqrt function for finding the square root of sum_squares_legs
#
#
# def hypotenuse(leg1, leg2):
#     sum_squares_legs = leg1 ** 2 + leg2 ** 2
#     len_hypotenuse = math.sqrt(sum_squares_legs)
#     return len_hypotenuse
#
#
# print('The length of the hypotenuse is', hypotenuse(3, 4))
#
#
# # The output: The length of the hypotenuse is 11.180339887498949
#
#
# # The sqrt function returns the float number. Now I got a correct answer to the question.
# # Also, I can round results by using round() function:
#
#
# def hypotenuse(leg1, leg2):
#     sum_squares_legs = leg1 ** 2 + leg2 ** 2
#     len_hypotenuse = math.sqrt(sum_squares_legs)
#     return round(len_hypotenuse, 2)
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))
#
# # The output: The length of the hypotenuse is 11.18

def hypotenuse(leg1, leg2):
    sum_squares_legs = leg1 ** 2 + leg2 ** 2
    len_hypotenuse = math.sqrt(sum_squares_legs)
    return round(len_hypotenuse, 2)


print('The length of the hypotenuse is', hypotenuse(3, 4))
print('The length of the hypotenuse is', hypotenuse(25, 5))
print('The length of the hypotenuse is', hypotenuse(16, 2.5))


