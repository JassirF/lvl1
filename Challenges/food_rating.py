# In a five-star review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.

# But what does each of the stars mean?

# Create a food rating system using an if/elif/else statement:

# rating greater than 4.5, print "Extraordinary"
# rating greater than 4, print "Excellent"
# rating greater than 3, print "Good"
# rating greater than 2, print "Fair"
# Everything else, print "Poor"

"""Let's see what our customers think of us"""
print('Gracias por haber venido a nuestro Restaurante, por favor complete esta encuesta de satisfaccion')
r = 10
while r != 0:
    review = input('Valore la experiencia del 1 al 5: ')
    if review == str(review):
        print('Porfavor, escribelo en numeros: ')
        review = input('Valore la experiencia del 1 al 5: ')
    else:
        review = int(review)
    if review == 4.5:
        print("Extraordinary")
        r = 0
    elif review == 4:
        print("Excellent")
        r = 0
    elif review == 3:
        print("Good")
        r = 0
    elif review == 2:
        print("Fair")
        r = 0
    else:
        print("Poor")
        r = 0