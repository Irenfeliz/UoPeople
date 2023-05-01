def exponentiation(number, power):
    result = number ** power
    # result = pow(number,power) - if use built-in
    return print(number, 'to the power of', power, 'equals', result)


exponentiation(3, 4)
exponentiation(10, 0)
exponentiation(10, 10)

