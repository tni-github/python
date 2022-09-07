# 4 - Реализуйте выдачу случайного числа не использовать random.randint
# и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime
# (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
from datetime import datetime


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def get_random(number_left, number_right, float_digits):
    while (is_number(number_left) == False or is_number(number_right) == False or float(number_right) <= float(number_left)):
        # проверка на корректность границ (являются числом)
        print('Некорректный ввод границ диапазона. Повторите ввод (первое число должно быть меньше второго)')
        number_left = input(
            'Введите первое число - левую границы интервала (диапазона): ')
        number_right = input(
            'Введите первое число - правую границы интервала (диапазона): ')
    else:
        while (float_digits.isdigit() == False or float(float_digits) < 0):
            # проверка на число, целочисленность и на положительность
            float_digits = input(
                'Введите корректное максимальное число знаков после запятой для числа из диапазона (целое, положительное):')
        else:
            random_number = 0
            interval_width = float(number_right) - float(number_left)
            random_interval = datetime.today().microsecond / 10**6
            random_number = round(
                (float(number_left) + interval_width*random_interval), int(float_digits))
            print(
                f'Случайное число из интервала [{number_left}; {number_right}] : {random_number}')


print('Введите ниже границы диапазона, из которого буде получать случайное число (первое число должно быть меньше второго')
number_left = input(
    'Введите первое число - левую границы интервала (диапазона): ')
number_right = input(
    'Введите первое число - правую границы интервала (диапазона): ')
float_digits = input(
    'Введите максимальное число знаков после запятой для числа из диапазона: ')
get_random(number_left, number_right, float_digits)
