# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import moduleFunc as module
import os
os.system("cls")


n = input('Введите число элементов последовательности: ')

n = int(module.enter_natural_number(n))
list_degree = [(3, i) for i in range(0, n)]
list_result = list(map(
    lambda list_degree_el: list_degree_el[0]**list_degree_el[1]*(-1)**list_degree_el[1], list_degree))
print(list_result)
