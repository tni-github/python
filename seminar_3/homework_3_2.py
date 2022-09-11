# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import homework_3_1 as module_func


def add_pairs_of_list() -> list:
    '''
    Поиск произведения пар чисел списка
    '''
    mult_pair = 0
    mult_pairs_list = []
    list_num = module_func.make_list_num()
    if len(list_num) == 0:
        return print(f'\nСписок пустой. Вы прервали ввод на первом элементе.')
    elif len(list_num) == 1:
        return print(f'Список {list_num} состоит всего из одного элемента, соответственно, пар нет.')
    else:
        for i in range(0, len(list_num) + 1):
            if i == len(list_num)-i-1:
                mult_pair = list_num[i] ** 2
            if i < len(list_num)/2:
                mult_pair = list_num[i] * list_num[len(list_num)-i-1]
            else:
                break
            mult_pairs_list.append(mult_pair)
        return print(f'Произведение пар чисел списка {list_num} найдено:{mult_pairs_list}')


add_pairs_of_list()
