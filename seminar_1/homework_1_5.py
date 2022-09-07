# 5-Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A(3, 6); B(2, 1) -> 5, 09
# - A(7, -5); B(1, -1) -> 7, 21
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_coordinate():
    n = input(f'\nВведите координату точки: ')
    while is_number(n) == False:
        n = input(
            f'\nНекорректный ввод. Введите координату точки: ')
    return float(n)


def find_distance(x1, y1, x2, y2):
    distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 3)
    return print(f'Расстояние между точкой A({x1}, {y1}) и точкой B({x2}, {y2}) равно: {distance}')


x1 = check_coordinate()
y1 = check_coordinate()
x2 = check_coordinate()
y2 = check_coordinate()

find_distance(x1, y1, x2, y2)
