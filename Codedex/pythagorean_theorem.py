"""Create a program that solves the Pythagorean Theorem:
c**2 = (a**2 + b**2)
"""
import math
print('Bienvenido al teorema de pitagoras, te va petar el cerebro')
print('Elige 2 de las variables que me daras, puede ser cualquiera, PERO DEBEN SER DOS!')


a = input('a = ')
b = input('b = ')
c = input('c = ')
while True:
    if a == '':
        b = int(b)
        c = int(c)
        print('Calculare a')
        a = math.sqrt((b**2+c**2))
        print(f'El resultado de a es: {a}')
    if b == '':
        a = int(a)
        c = int(c)
        print('Calculare b')
        b = math.sqrt((a**2+c**2))
        print(f'El resultado de b es: {b}')
    if c == '':
        a = int(a)
        b = int(b)
        print('Calculare c')
        c = math.sqrt((a**2+b**2))
        print(f'El resultado de c es: {c}')
    elif a or b or c == 'salir':
        print('Gracias por usarme')
        break
    else:
        print('Gracias por usarme')
        break
