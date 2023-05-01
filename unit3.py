def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


num = int(input()) # requesting an integer number

if num > 0:
    countdown(num)  # when number is positive we count down
else:
    countup(num)  # when number is negative or zero we count up.
    # In case of zero, it doesn't matter which function we call,
    # because zero triggers Blastoff.


