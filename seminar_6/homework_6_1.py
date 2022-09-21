# 1- Определить, присутствует ли в заданном списке строк, некоторое число

import os
os.system("cls")

list_str = ['ежи8к', 'за1яц', 'корона 1']
number = 1

list_str_filtered = list(
    filter(lambda list_el: str(number) in list_el, list_str))


def result(list_str, list_str_filtered, number):
    if len(list_str_filtered) >= 1:
        print(f'Число {number} есть в списке строк {list_str}.')
    else:
        print(f'Число {number} отсутствует в списке строк {list_str}.')


result(list_str, list_str_filtered, number)
