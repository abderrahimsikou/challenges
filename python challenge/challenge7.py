import math
x1 = float(input('Enter 1:'))
x2 = float(input('Enter 2:'))
x3 = float(input('Enter 3:'))
x4 = float(input('Enter 4:'))

dist = math.sqrt((x2 - x1) **2 +(x3 - x4) **2)
print(f'The distance: {dist:.2f}')