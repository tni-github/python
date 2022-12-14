# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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


def sum_odd() -> float:
    '''
    Получение суммы элементов списка, стоящих на нечетной позиции
    '''
    sum_odd_el = 0
    make_list_num()
    if len(list_num) == 0:
        return print(f'\nСписок пустой. Вы прервали ввод на первом элементе.')
    elif len(list_num) == 1:
        return print(f'\nСписок {list_num} состоит всего из одного элемента, нечетных позиций нет.')
    else:
        for i in range(1, len(list_num)):
            if i == 1 or i % 2 != 0:
                sum_odd_el += list_num[i]
        return print(f'\nСумма элементов списка {list_num}, стоящих на нечетной позиции равна: {sum_odd_el}')


if __name__ == '__main__':
    sum_odd()
