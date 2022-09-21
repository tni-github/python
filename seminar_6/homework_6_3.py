# 3- Найти расстояние между двумя точками пространства
# (числа вводятся через пробел)

# Пример:

# - A(3, 6); B(2, 1) -> 5, 09
# - A(7, -5); B(1, -1) -> 7, 21

import os
os.system("cls")


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_coordinate():
    n = input(f'\nВведите координату точки: ')
    while is_number(n) == False:
        n = input(
            f'\nНекорректный ввод. Введите координату точки: ')
    return float(n)

# find_distance = lambda x1, y1, x2, y2: round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 3)

# ПОЧЕМУ-ТО КОД ИЗ СТРОКИ 28 АВТОМАТОМ МЕНЯЕТСЯ НА КОД ИЗ СТРОКИ 32


def find_distance(x1, y1, x2, y2): return round(
    ((x2 - x1)**2 + (y2 - y1)**2)**0.5, 3)


x1 = get_coordinate()
y1 = get_coordinate()
x2 = get_coordinate()
y2 = get_coordinate()

result = find_distance(x1, y1, x2, y2)
print(result)
