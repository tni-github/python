# 4 - Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def check_quarter(num):
    while is_number(num) == False or int(num) < 1 or int(num) > 4:
        num = input(
            'Некорректный ввод. Введите арабскую цифру от 1 до 4 (вкл.): ')
    else:
        num = int(num)
        if num == 1:
            print('0 < x < ∞, 0 < y < ∞')
        elif num == 2:
            print('0 < x < ∞, -∞ < y < 0')
        elif num == 3:
            print('-∞ < x < 0, -∞ < y < 0')
        elif num == 4:
            print('-∞ < x < 0, 0 < y < ∞')


n_base = " "
n_foot = "_"
print('\nЧетверти координатной плоскости:\n', sep='\n\n')
print(f'{n_base*9}|{n_base*9}', sep='\n\n')
print(f'{n_base*4}4{n_base*4}|{n_base*4}1{n_base*4}', sep='\n')
print(f'{n_foot*9}|{n_foot*9}', sep='\n')
print(f'{n_base*9}|{n_base*9}', sep='\n')
print(f'{n_base*4}3{n_base*4}|{n_base*4}2{n_base*4}', sep='\n')
print(f'{n_base*9}|{n_base*9}', sep='\n')

quarter = input(f'\nВведите номер четверти, для которой хотите узнать диапазон возможных координат точек. Обратите внимание: должна быть арабская цифра от 1 до 4 (вкл.)! Ваш вариант: ')

check_quarter(quarter)
