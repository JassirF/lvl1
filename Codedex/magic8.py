"""This programs create a game where you Q and it A with some random text generated randomly over a 
fixed database"""
import random
n1 = ('Si, definitivamente.')
n2 = ('Rotundamente no.')
n3 = ('Sin duda.')
n4 = ('Mi magia esta nublada, tal vez luego.')
n5 = ('Pregunta mas tarde.')
n6 = ('Mejor que no lo sepas.')
n7 = ('Mis fuentes dicen que no.')
n8 = ('No tiene buena pinta.')
n9 = ('No lo creo.')

q = input ('Preguntame lo que quieras: ')
# if input is True:
# Asi no funciona, no se por que
if q is False:
    print ('¿Seguro que no tienes preguntas?')
if q is not False:
    print('Le estamos preguntando al genio... espera')
    print(f'Tu pregunta era: {q}')
    rng = random.randint(1,9)
    if rng == 1:
        print(f'El genio dice: {n1}')
    if rng == 2:
        print(f'El genio dice: {n2}')
    if rng == 3:
        print(f'El genio dice: {n3}')
    if rng == 4:
        print(f'El genio dice: {n4}')
    if rng == 5:
        print(f'El genio dice: {n5}')
    if rng == 6:
        print(f'El genio dice: {n6}')
    if rng == 7:
        print(f'El genio dice: {n7}')
    if rng == 8:
        print(f'El genio dice: {n7}')
    if rng == 9:
        print(f'El genio dice: {n9}')