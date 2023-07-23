# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

# Create a weight conversion program that:

# Ask the user what their Earth weight is.
# Ask the user for a number that correlates with a planet.
# Calculate the user's weight on the destination planet.
# To calculate user's weight:

# destination weight=Earth weight × relative gravity

Mercury = 0.38
Venus = 0.91
Mars = 0.38
Jupiter = 2.53
Saturn = 1.07
Uranus = 0.89
Neptune = 1.14

print("Welcome to the interestellar travel agency, we will need some data to continue.")

e_weight = int(input('Earth weight: '))

planet_id = int(input('Planet ID: '))

if planet_id == 1:
    d_weight = e_weight*Mercury
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 2:
    d_weight = e_weight*Venus
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 3:
    d_weight = e_weight*Mars
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 4:
    d_weight = e_weight*Jupiter
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 5:
    d_weight = e_weight*Saturn
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 6:
    d_weight = e_weight*Uranus
    print('Your package weight at destination is: ', d_weight)
elif planet_id == 7:
    d_weight = e_weight*Neptune
    print('Your package weight at destination is: ', d_weight)
