"""Harry Potter's son will enter Hogwarts School of Witchcraft and Wizardry
this code will be what the Sorting Hat will tell the students of 1st year
when picking their House og Magic"""

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Bienvenidos alumnos, a la escuela Hogwarts de Magia y Hechizeria, hoy es un dia muy especial')
print('pues elegiran con ayuda del \'Sombrero seleccionador\' cual sera vuestra casa de aqui en')
print('adelante, pasad al salon principal, donde les esperara el director Albus Dumbledore y el')
print('resto de profesores de la escuela.')
nombre = input('Dime cual es tu nombre, joven mago/maga: ')
if nombre == (''):
    print('Que me digas tu nombre, no pongas a prueba mi paciencia')
    nombre = input('')
    print('Ok...')
while True:
    print(f'Bienvenido/a {nombre}, elige las respuestas por su numero')
    print('¿Te gusta mas el atardecer o el amanecer?')
    print(' 1) Amanecer')
    print(' 2) Atardecer')
    ch1 = int(input('Elige: '))
    if ch1 == 1:
        Gryffindor += 1
        Ravenclaw += 1
    else:
        Hufflepuff += 1
        Slytherin += 1
    print('¿Cuando mueras querras ser recordado de que manera?')
    print(f' 1) {nombre} el/la Bueno/a')
    print(f' 2) {nombre} el/la Grande')
    print(f' 3) {nombre} el/la Sabio/a')
    print(f' 4) {nombre} el/la Intrepido/a')
    ch2 = int(input(''))
    if ch2 == 1:
        Hufflepuff += 2
    elif ch2 == 2:
        Slytherin += 2
    elif ch2 == 3:
        Ravenclaw += 2
    elif ch2 == 4:
        Gryffindor += 2
    print('¿Que instrumento te gusta mas?')
    print(' 1) El violin')
    print(' 2) La trompeta')
    print(' 3) El piano')
    print(' 4) La bateria')
    ch3 = int(input(''))
    if ch3 == 1:
        Slytherin += 4
    if ch3 == 2:
        Hufflepuff += 4
    if ch3 == 3:
        Ravenclaw += 4
    if ch3 == 4:
        Gryffindor += 4

    break
score = max(Gryffindor,Slytherin,Hufflepuff,Ravenclaw)
if score == Gryffindor:
    print('¡Gryffindor!')
if score == Slytherin:
    print('¡Slytherin!')
if score == Hufflepuff:
    print('¡Hufflepuff!')
if score == Ravenclaw:
    print('¡Ravenclaw!')
print('Esa sera tu casa de ahora en adelante joven mago/a, te esperan muchas aventuras, suerte!')
