# Snapple is a famous tea drink brand from Queens, New York. Each bottle cap comes with a silly fun fact.

# Here are six Snapple facts:

# Flamingos turn pink from eating shrimp.
# The only food that doesn’t spoil is honey.
# Shrimp can only swim backwards.
# The lifespan of a taste bud is about 10 days.
# It is impossible to sneeze while sleeping.
# It is illegal to sing off-key in North Carolina.
# Use the random module to create a number from 0 to 5.

# Then use an if/elif/else statement to print out one of these random facts.
import random
num = 0
for num in range (3):
    num = random.randint(1, 7)
    if num == 7:
        print ('Flamingos turn pink from eating shrimp.')
    if num == 6:
        print ('The only food that doesn\'t spoil is honey.')
    if num == 5:
        print ('Shrimp can only swim backwards.')
    if num == 4:
        print ('The lifespan of a taste bud is about 10 days.')
    if num == 3:
        print ('It is impossible to sneeze while sleeping.')
    if num == 2:
        print ('It is illegal to sing off-key in North Carolina.')
    if num == 1:
        print ('Use the random module to create a number from 0 to 5.')   
