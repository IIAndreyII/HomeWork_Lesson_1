# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
x = int(input('X = '))
y = int(input('Y = '))

print('Введите координаты точки B')
x1 = int(input('X = '))
y1 = int(input('Y = '))

import math
d = math.sqrt(pow((x1-x),2)+pow((y1-y),2))

print(round(d,2))

