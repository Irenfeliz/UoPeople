import math
def my_sqrt(a):
    x = a / 2
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    return x


def test_sqrt():
    for a in range(1, 26):
        diff = abs(my_sqrt(a) - math.sqrt(a))
        print(f"a = {a} | my_sqrt(a) = {my_sqrt(a)} | math.sqrt(a) = {math.sqrt(a)} | diff = {diff}")

test_sqrt()
