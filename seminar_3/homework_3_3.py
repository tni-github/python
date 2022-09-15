# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


import homework_3_1 as module_func
import os
os.system("cls")


def find_diff_max_min() -> float:
    '''
    Поиск разницы между максимальным и минимальным значением 
    дробной части элементов списка
    '''
    list_num_div = []
    list_num = module_func.make_list_num()
    first_list_num = list_num.copy()
    diff_max_min = 0
    if len(list_num) == 0:
        return print(f'\nСписок пустой. Вы прервали ввод на первом элементе.')
    elif len(list_num) == 1:
        return print(f'Список {list_num} состоит всего из одного элемента, соответственно, поиск разницы между максимальным и минимальным значением дробной части элементов списка не имеет смысла.')
    else:
        for i in range(0, len(list_num)):
            list_num[i] = round(abs(float(list_num[i])), 7)
            list_num_div.append(round(list_num[i] - int(list_num[i]), 7))
        # return print(list_num_div)
            min_el = list_num_div[0]
            max_el = list_num_div[0]
        for i in range(1, len(list_num_div)):
            if list_num_div[i] > max_el:
                max_el = list_num_div[i]
            if list_num_div[i] < min_el:
                min_el = list_num_div[i]
        diff_max_min = round(max_el - min_el, 7)
        return print(f'Разница между максимальным ({max_el}) и минимальным  ({min_el}) значением дробной части элементов списк {first_list_num} равна: {max_el} - {min_el} = {diff_max_min}')


find_diff_max_min()
