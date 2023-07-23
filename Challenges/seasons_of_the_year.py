# Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call.

# Ask the user the month number using the input() function.

# Check for the four seasons using an if/elif/else statement and logical operators:

# month is 1, 2, 3, print "Winter ❄️"
# month is 4, 5, 6, print "Spring 🌱"
# month is 7, 8, 9, print "Summer 🌻"
# month is 10, 11, 12, print "Autumn 🍂"
# Everything else is "Invalid"

m = input('Dime en que mes estamos para decirte la estacion: ')
if m in ['Enero', 'Febrero', 'Marzo']:
    print('Invierno')
elif m in ['Abril', 'Mayo', 'Junio']:
    print('Primavera')
elif m in ['Julio', 'Agosto', 'Septiembre']:
    print('Verano')
elif m in ['Octubre', 'Noviembre', 'Diciembre']:
    print('Invierno')
if m in ['1', '2', '3']:
    print('Invierno')
elif m in ['4', '5', '6']:
    print('Primavera')
elif m in ['7', '8', '9']:
    print('Verano')
elif m in ['10', '11', '12']:
    print('Otono')
else:
    print('Eres de otro planeta loco')
