"""Random coin flipper, this loop execute 5 times"""

import random
for num in range(5):
    # RNGesus will give us a random number that is either 0 or 1
    num = random.randint(0, 1)
    if num > 0.5:
        print('Heads')
    else:
        print('Tails')
