# I will use the idea from my example for the Unit 3 discussion forum.
# Now I have written a function to check if a member is suitable
# for a school swimming team that accepts girls only aged 10 - 16:

def girls_swimming_team(age, sex):
    if sex == 'female' and 10 <= age <= 16:
        return
    else:
        return False

age = 13
sex = 'female'

if girls_swimming_team(age,sex):
    print('You are accepted!')
else:
    print('Sorry, you are not accepted')

# The output: Sorry, you are not accepted