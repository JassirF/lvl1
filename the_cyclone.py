"""A program to know how much money the user have and his height
the program will choose over a fixed answer what to tell you giving
each variable"""
print('Bienvenido a la \'Gran Montana Rusa\', para pasar ')
print('debes medir mas de 137cm, la entrada cuesta 10 EUR')
height = int(input('Cual es tu altura: '))
money = int (input('Cuanto dinero tienes: '))
if height >= 137 and money >= 10:
    print('Disfruta el viaje')
if height < 137 and money <10:
    print('No tienes la altura y no puedes pagarte el viaje')
elif height < 137:
    print('No eres lo suficientemente alto')
elif money < 10:
    print('Te falta dinero')
print('Gracias por venir!')
