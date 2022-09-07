# 3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 2
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_point_position(x, y):
    while (is_number(x) == False):
        x = input('Некорректный ввод. Введите координату X: ')
    while (is_number(y) == False):
        y = input('Некорректный ввод. Введите координату Y: ')
    if float(x) > 0 and float(y) > 0:
        print(
            f'\nТочка с координатами ({x}, {y}) находится в первой (I) четверти')
    elif float(x) > 0 and float(y) < 0:
        print(
            f'\nТочка с координатами ({x}, {y}) находится во второй (II) четверти')
    elif float(x) < 0 and float(y) < 0:
        print(
            f'\nТочка с координатами ({x}, {y}) находится в третьей (III) четверти')
    elif float(x) < 0 and float(y) > 0:
        print(
            f'\nТочка с координатами ({x}, {y}) находится в четвертой (IV) четверти')
    elif float(x) == 0 and (float(y) > 0 or float(y) < 0):
        print(f'\nТочка с координатами ({x}, {y}) находится на оси Y')
    elif float(y) == 0 and (float(x) > 0 or float(x) < 0):
        print(f'\nТочка с координатами ({x}, {y}) находится на оси Y')
    else:
        print(
            f'\nТочка с координатами ({x}, {y}) находится на пересечении осей координат.', sep='\n\n')


x = input('Введите координату X: ')
y = input('Введите координату Y: ')

check_point_position(x, y)


n_base = " "
n_foot = "_"
print('\nЧетверти координатной плоскости:\n', sep='\n\n')
print(f'{n_base*9}|{n_base*9}', sep='\n\n')
print(f'{n_base*3}IV{n_base*4}|{n_base*4}I{n_base*4}', sep='\n')
print(f'{n_foot*9}|{n_foot*9}', sep='\n')
print(f'{n_base*9}|{n_base*9}', sep='\n')
print(f'{n_base*3}III{n_base*3}|{n_base*4}II{n_base*3}', sep='\n')
print(f'{n_base*9}|{n_base*9}', sep='\n')
