"""Fizz-buzz my frrrriend, lets see how creative Jassir is (p.s: I am Michelangelo)"""
# Create a fizz_buzz.py program that outputs numbers from 1 to 100. Here's the catch:

# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".


for a in range(1, 101):

    if (a%3 == 0) and (a%5 == 0):
        print('Fizz-Buzz')
    elif a%3 == 0:
        print('Fizz')
    elif a%5 == 0:
        print('Buzz')
    else:
        print(a)
