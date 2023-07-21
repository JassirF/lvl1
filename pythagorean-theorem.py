"""Create a hypotenuse.py program that asks the user for two numbers, a and b, and calculates the hypotenuse using the Pythagorean equation, rewritten like so:

c**2= sqr.root(a**2 + b**2)
"""
import math
print('Bienvenido al teorema de pitagoras, te va petar el cerebro')
print('Elige 2 de las variables que me daras, puede ser cualquiera, PERO DEBEN SER DOS!')


a = (input('a = '))
b = (input('b = '))
c = (input('c = '))
while True:
    if a == '':
        b = int(b)
        c = int(c)
        if b or c == 'salir':
            break
        print('Calculare a')
        a = math.sqrt((b**2+c**2))
        print('Esta es c:', a)
    if b == '':
        a = int(a)
        c = int(c)
        if a or c == 'salir':
            break
        print('Calculare b')
        b = math.sqrt((a**2+c**2))
        print('Esta es c:', b)
    if c == '':
        a = int(a)
        b = int(b)
        if a or b == 'salir':
            break
        print('Calculare c')
        c = math.sqrt((a**2+b**2))
        print('Esta es c:', c)
    else:
        break

