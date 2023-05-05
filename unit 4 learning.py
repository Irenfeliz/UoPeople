# Let’s declare the function hypotenuse with 2 parameters leg1 and leg2:
# def hypotenuse(leg1, leg2):
#     return 0
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))
# syntactically correct, and it returns the value (zero), but not that value we need.

# Now let's find the sum of the squares of the lengths of the legs
# def hypotenuse(leg1, leg2):
#     sum_squares_legs = leg1 ** 2 + leg2 ** 2
#     return sum_squares_legs
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))

# Now there is another value, the result of calculation of the sum. But it is not an answer on the task.
# So now we need to extract a square from the sum_squares_legs to find the length of the hypotenuse

# for extraction a square I'll use math module, so I should import it
import math

# creating new local variable len_hypotenuse and use sqrt function for finding the square root of sum_squares_legs
# def hypotenuse(leg1, leg2):
#     sum_squares_legs = leg1 ** 2 + leg2 ** 2
#     len_hypotenuse = math.sqrt(sum_squares_legs)
#     return len_hypotenuse
#
#
# print('The length of the hypotenuse is', hypotenuse(10, 5))

# output: The length of the hypotenuse is 11.180339887498949

def hypotenuse(leg1, leg2):
    sum_squares_legs = leg1 ** 2 + leg2 ** 2
    len_hypotenuse = math.sqrt(sum_squares_legs)
    return round(len_hypotenuse, 2)


print('The length of the hypotenuse is', hypotenuse(35, 45))




