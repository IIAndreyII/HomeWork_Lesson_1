# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти системы координат на плоскости: '))

if x == 1:
    print('X > 0: Y > 0.')
elif x == 2:
    print('X < 0: Y > 0.')
elif x == 3:
    print('X < 0: Y < 0.')
elif x == 4:
    print('X > 0: Y < 0.')

else:
    print('Введены не корректные данные')
