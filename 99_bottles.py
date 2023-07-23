"""99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall."""

bottles = 99

for a in range (1, 100):
    print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
    bottles -= 1
    print(f'Take one down and pass it around, {bottles} of beer on the wall.')
