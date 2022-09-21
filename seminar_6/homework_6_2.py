# 2 - Найти сумму чисел списка стоящих на нечетной позиции

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce
import os
os.system("cls")


def make_list_num() -> list:
    '''
    Получение списка
    '''
    global list_num
    list_num = []
    n = input(
        'Введите нужное количество элементов списка. Например, для списка [1, 45, 5] - количество равно 3 (трем). Ваше количество: ')
    while (n.isdigit() == False or float(n) <= 0):
        n = input(
            'Некорректный ввод. Введите нужное количество элементов списка: ')
    for i in range(1, int(n)+1):
        num = input(
            'Введите число, которое будет в списке. Для досрочного прекращения ввода, завершения формирования списка - поставьте точку (.) ')
        if num == '.':
            break
        try:
            float(num)
            list_num.append(float(num))
        except ValueError:
            num = input(
                'Некорректный ввод. Для досрочного прекращения ввода, завершения формирования списка - поставьте точку (.). Иначе введите целое положительное число, которое будет в списке: ')
            if num == '.':
                break
    return list_num


def check_is_index_odd(list_num_tuple_el):
    if list_num_tuple_el[0] == 1 or list_num_tuple_el[0] % 2 != 0:
        return True
    else:
        return False


def sum(list_num_tuple):
    if list_num_tuple[1]:
        return True
    else:
        return False


def sum_odd() -> float:
    '''
    Получение суммы элементов списка, стоящих на нечетной позиции
    '''
    sum_odd_el = 0
    list_num = make_list_num()
    if len(list_num) == 0:
        return print(f'\nСписок пустой. Вы прервали ввод на первом элементе.')
    elif len(list_num) == 1:
        return print(f'\nСписок {list_num} состоит всего из одного элемента, нечетных позиций нет.')
    else:
        list_filtered = list(
            filter(check_is_index_odd, list(enumerate(list_num))))
        print(list_filtered)
        sum_odd_el = list(
            list(map(lambda list_filtered: float(list_filtered[1]), list_filtered)))
        # sum_print = sum(sum_odd_el)
        sum_odd_el = reduce(lambda x, y: x+y, sum_odd_el)

        return print(f'\nСумма элементов списка {list_num}, стоящих на нечетной позиции равна: {sum_odd_el}')


# НЕ ПОНИМАЮ ПОЧЕМУ НЕ РАБОТАЕТ sum_print = sum(sum_odd_el)
# ВРОДЕ КАК sum([2.0, 4.0]) (например) ДОЛЖНО БЫТЬ РАВНО 6
# (а возвращается True)
sum_odd()
