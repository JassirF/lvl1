# U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨

# First, ask the user their grade using the input() function.

# Create a 4-year high school grade system using an if/elif/else statement:

# grade is 9, print "Freshman"
# grade is 10, print "Sophomore"
# grade is 11, print "Junior"
# grade is 12, print "Senior"
# Everything else is "TBD"
print ('Bienvenido al instituto, porfavor dinos en que ano estas para decirte que eres')
gr = int(input('Escribe aqui: '))
if gr == 9:
    print('Freshman')
elif gr == 10:
    print('Sophomore')
elif gr == 11:
    print('Junior')
elif gr == 12:
    print('Senior')
else:
    print('TBD')