# 1 - Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import moduleFunc as mod

# очистка консоли
import os
os.system("cls")
# очистка консоли


def make_prime_numbers(n: int) -> list:
    '''
    Получение списка простых множителей  числа
    '''
    mod.enter_natural_number(n)
    prime_number_list = mod.make_prime_number_list(n)
    first_num = n
    prime_factor_list = []
    for i in range(1, len(prime_number_list)):
        factor = prime_number_list[i]
        while (int(n) % factor == 0):
            prime_factor_list.append(factor)
            n = int(n) / factor
    if len(prime_factor_list) == 1:
        print(
            f'Простые множители числа {first_num} является самим числом {prime_factor_list[0]}')
    else:
        print(
            f'Список простых множителей числа {first_num}: {prime_factor_list}')
    return prime_factor_list


print('Программа выдает список простых множителей натурального числа (исключая 1).')
num = input('Введите натуральное число (целое положительное): ')
make_prime_numbers(num)
