import math

# # Let's define the function and put an expression in a return statement:
#
#
# def quadratic_equation(a, b, c):
#    x1 = 0
#    x2 = 0
#    return f'The roots of the quadratic equation are {x1} and {x2}'
#
#
#
#
# print(quadratic_equation(4, 6, 2))
#
# # The output: The roots of the quadratic equation are 0 and 0
# # The function is defined, run, and returns a result.
# # Let's find a discriminant for the quadratic equation:
#
#
# def quadratic_equation(a, b, c):
#    x1 = 0
#    x2 = 0
#    discriminant = b ** 2 - 4 * a * c
#    # return f'The roots of the quadratic equation are {x1} and {x2}'
#    return f'The discriminant for the quadratic equation is {discriminant}'
#
#
#
#
# print(quadratic_equation(4, 2, 4))
#
#
# # The output: The discriminant for the quadratic equation is -60
#
#
# # I should check the value of discriminant and make conditions:
# def quadratic_equation(a, b, c):
#    x1 = 0
#    x2 = 0
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant > 0:
#        pass
#    elif discriminant == 0:
#        pass
#    else:
#        return f'The quadratic equation does not have roots'
#    # return f'The roots of the quadratic equation are {x1} and {x2}'
#    return f'The discriminant for the quadratic equation is {discriminant}'
#
#
#
#
# print(quadratic_equation(4, 2, 4))
#
#
# # The output: The quadratic equation does not have a roots
#
#
# # I've added 3 conditions; if d > 0, the equation has 2 roots (now I put a pass in this condition),
# # If d = 0, the equation has 1 root (also passed for now)
# # and if d < 0, there are no roots for the equation - I made an individual return for this condition.
#
#
# # Let's make a solution for the first condition (if-statement):
# def quadratic_equation(a, b, c):
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant > 0:
#        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#        return f'The roots of the quadratic equation are {x1} and {x2}'
#    elif discriminant == 0:
#        pass
#    else:
#        return f'The quadratic equation does not have roots'
#
#
#
#
# print(quadratic_equation(4, 6, 2))
#
#
# # The output: The roots of the quadratic equation are -0.5 and -1.0
#
#
# # Now the second condition (elif-statement):
#
#
# def quadratic_equation(a, b, c):
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant > 0:
#        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#        return f'The roots of the quadratic equation are {x1} and {x2}'
#    elif discriminant == 0:
#        x = -b / (2 * a)
#        return f'The quadratic equation has one root equal {x}'
#    else:
#        return f'The quadratic equation does not have roots'
#
#
#
#
# print(quadratic_equation(1, 2, 1))
#
#
# # The output: The quadratic equation has one root equal to -1.0
#
#
# def quadratic_equation(a, b, c):
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant > 0:
#        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#        return f'The roots of the quadratic equation are {x1} and {x2}'
#    elif discriminant == 0:
#        x = -b / (2 * a)
#        return f'The quadratic equation has one root equal {x}'
#    else:
#        return f'The quadratic equation does not have roots'
#
#
#
#
# print(quadratic_equation(1, 2, -1))
#
#
# # The output: The roots of the quadratic equation are 0.41421356237309515 and -2.414213562373095
#
#
# # I can use round func to return rounded values:
#
#
# def quadratic_equation(a, b, c):
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant > 0:
#        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#        return f'The roots of the quadratic equation are {round(x1, 2)} and {round(x2, 2)}'
#    elif discriminant == 0:
#        x = -b / (2 * a)
#        return f'The quadratic equation has one root equal {round(x, 2)}'
#    else:
#        return f'The quadratic equation does not have roots'
#
#
#
#
# print(quadratic_equation(1, 2, -1))
#
#
# #The output: The roots of the quadratic equation are 0.41 and -2.41


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f'The roots of the quadratic equation are {round(x1, 2)} and {round(x2, 2)}'
    elif discriminant == 0:
        x = -b / (2 * a)
        return f'The quadratic equation has one root equal {round(x, 2)}'
    else:
        return f'The quadratic equation does not have roots'


print(quadratic_equation(10, 3, 5))
print(quadratic_equation(-1, -25, 25))
print(quadratic_equation(1, 2, 1))