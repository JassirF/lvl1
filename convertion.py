"""We will be converting different national currencies into EUR and USD"""
sol_per = int(input('Cuantos soles peruanos tienes: '))
peso_col = int(input('Cuantos pesos colombianos tienes: '))
real_bra = int(input('Cuantos reales brasilenos tienes: '))

if sol_per == int(sol_per):
    print ('Con los soles que tienes puedes cambiarlos a: ')
    print (sol_per*0.2507, 'euros')
    print (sol_per*0.2791, 'dolares')
if peso_col == int(peso_col):
    print ('Con los pesos que tienes puedes cambiarlos a: ')
    print(peso_col*0.00023,'euros')
    print(peso_col*0.00025,'dolares')
if real_bra == int(real_bra):
    print ('Con los reales que tienes puedes cambiarlos a: ')
    print(peso_col*0.1879,'euros')
    print(peso_col*0.2092,'dolares')