<<<<<<< HEAD
import math
figure = input()
area = 'Not defined'
if figure == ('square'):
    side = float(input())
    area = side * side
    print(f'{area:.3f}')
elif figure == 'rectangle':
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
    print(f'{area:.3f}')
elif figure == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height/2
    print(f'{area:.3f}')
print(f'{area}')
=======
import math
figure = input()
area = 'Not defined'
if figure == ('square'):
    side = float(input())
    area = side * side
    print(f'{area:.3f}')
elif figure == 'rectangle':
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
    print(f'{area:.3f}')
elif figure == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height/2
    print(f'{area:.3f}')
print(f'{area}')
>>>>>>> f5e08af265b4e5302a530dba1d0ac93840d06fcc
