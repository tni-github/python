# 2 - Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import moduleFunc as mod
import os
os.system("cls")


def find_unique_elems(list_input: list) -> list:
    '''
    Функция отсеивает нечисловые значения и выдает списком те элементы, которые являются уникальными (неповторяющимися).
    Например:
    1 - Список, который Вы ввели: 1.23,1,1,,2,2,, (поставлены лишние запятые в середине и в конце последовательности), будет преобразован в числовую последовательность: [1.23, 1, 1, 2, 2]. В итоге список неповторяющихся элементов указанной последней последовательности: [1.23, 1, 2]
    2 - Список, который Вы ввели: ,,1,,1,1,2,2,1,1,1,,1, (поставлены лишние запятые в начале и середине послежовательности), будет преобразован в числовую последовательность: [1, 1, 1, 2, 2, 1, 1, 1, 1]. В итоге список неповторяющихся элементов указанной последней последовательности: [1, 2]
    3 - Список, который Вы ввели: s,fsfd.dfsff,1,2 (поставлены лишние запятые, а также строковые значения), будет преобразован в числовую последовательность:[1, 2]. Cписок неповторяющихся элементов указанной последней последовательности: [1, 2]
    '''
    i = 0
    counter = 0
    len_list = len(list_input)
    unique_elems_list = []
    while i < len_list:
        try:
            float(list_input[i])
            counter = mod.null_counter(float(list_input[i]))
            list_input[i] = round(float(list_input[i]), counter)
            i += 1
        except ValueError:
            i += 1
    changed_list = list_input.copy()
    str_quantity = mod.get_str_quantity(changed_list)
    while str_quantity > 0:
        for i in range(1, str_quantity + 2):
            mod.clear_list(changed_list, str_quantity)
        str_quantity = mod.get_str_quantity(changed_list)
    if len(changed_list) == 0:
        return print('Вы не ввели ни одного числового значения! Программа завершена.')
    else:
        for i in range(0, len(changed_list)):
            if changed_list[i] - int(changed_list[i]) == 0:
                changed_list[i] = int(changed_list[i])
            unique_elems_list.append(changed_list[i])
            if unique_elems_list.count(changed_list[i]) > 1:
                unique_elems_list.pop(len(unique_elems_list)-1)
    print(
        f'Список, который Вы ввели: {list_input}, был преобразован в числовую последовательность: {changed_list}. Cписок неповторяющихся элементов числовой последовательности: {unique_elems_list}.')
    return unique_elems_list


print('Программа выдает список неповторяющихся элементов заданной числовой последовательности.')
print('Если введете не только числа, все элементы, кроме чисел, будут удалены из последовательности.')
list_num = input(
    'Введите числа списка через запятую (в случае десятичных чисел дробная часть отделяется от целой точкой, например 1.23): ').split(',')

find_unique_elems(list_num)
