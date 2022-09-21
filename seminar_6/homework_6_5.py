# 5- Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import os
os.system("cls")


def make_list_num() -> list:
    '''
    Получение списка
    '''
    # global list_num
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


def add_pairs_of_list() -> list:
    '''
    Поиск произведения пар чисел списка
    '''
    mult_pairs_list = []
    list_num = make_list_num()
    if len(list_num) == 0:
        return print(f'\nСписок пустой. Вы прервали ввод на первом элементе.')
    elif len(list_num) == 1:
        return print(f'Список {list_num} состоит всего из одного элемента, соответственно, пар нет.')
    else:
        mult_pairs_list = [list_num[i]*list_num[len(list_num)-i-1]
                           for i in range(0, len(list_num)//2 + len(list_num) % 2)]
        return print(f'Произведение пар чисел списка {list_num} найдено:{mult_pairs_list}')


add_pairs_of_list()
