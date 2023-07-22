"""This program check students grades and give the letter of calification"""
grade = int(input('Escribe la nota del alumno: '))

if  grade >= 90 <=100:
    print('A')
elif grade >=80 <=90:
    print('B')
elif grade >=70 <=80:
    print('C')
elif grade >=60 <=70:
    print('D')
elif grade >=50 <=60:
    print('E')
else:
    print ('Failed')

# Next level step is to configure this Python file with external sources, like Excell or a DB