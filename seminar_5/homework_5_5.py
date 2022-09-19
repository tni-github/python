# Создать программу, считывающую два полинома из двух файлов
# и записывающая в третий файл их сумму.

from typing import List, Optional
import moduleFunc as mod
import os

# очистка консоли
os.system("cls")
# очистка консоли


polinom_1 = mod.remove_spaces_in_string(mod.read_file('polinom1.txt'))
polinom_2 = mod.remove_spaces_in_string(mod.read_file('polinom2.txt'))


def find_polynomial_degree(pol):
    '''
    Функция находит и возвращает степень полинома.
    Поиск осуществляется по следующему принципу:
    та степень, которая стоит у "x" перед первым плюсом,
    и будет равна степени полинома.
    Учтено, что икс случайно могут поставить не на английском,
    а на русском языке.
    '''
    try:
        pol.index('+')
        index_of_first_plus = pol.index('+')
        # print(index_of_first_plus)
        if pol[index_of_first_plus-1] == 'x' or pol[index_of_first_plus-1] == 'х':
            polynomial_degree = 1
        else:
            polynomial_degree = pol[index_of_first_plus-1]
    except ValueError:
        polynomial_degree = pol[pol.index('=')-1]
    return polynomial_degree


def make_x_list(degree_1: Optional[int], degree_2: Optional[int]) -> List[str]:
    '''
    Функция возвращает список умножаемых на коэффициенты "x"-ов
    в нужных степенях в порядке убывания от максимальной из степеней
    двух слагаемых полиномов.
    '''
    x_list = []
    if degree_1 >= degree_2:
        degree = degree_1
    else:
        degree = degree_2
    for i in range(0, int(degree) + 1):
        if i == 0:
            x_list.append('1')
        if i == 1:
            x_list.append('x')
        if i > 1:
            x_list.append(f'x^{i}')
    x_list = list(reversed(x_list))
    print(x_list)
    return (x_list)

# ДОБАВИТЬ НУЛЕВЫЕ ЭЛЕМЕНТЫ ПРИ СРАВНЕНИИ СО СПИСКОМ КОЭФФИЦИЕНТОВ


def find_coefficients(pol: Optional[str], x_list: List[str]) -> List[str]:
    '''
    Функция возвращает список список слагаемых левой части полинома.
    '''
    coefficients_list = []
    remove_right_part_pol = pol[:-2]
    try:
        list_left_part = remove_right_part_pol.split('+')
    except ValueError:
        list_left_part = remove_right_part_pol
    # print(list_left_part)
    if len(x_list) > len(list_left_part):
        for i in range(0, len(list_left_part)):
            try:
                list_left_part[i].index('*')
                index_mult = list_left_part[i].index('*')
                coeff = list_left_part[i][:index_mult]
                coefficients_list.append(coeff)
            except ValueError:
                if list_left_part[i].isdigit() == True:
                    coefficients_list.append(0)
                if i == len(x_list):
                    index_last = list_left_part.index('=')
                    coefficients_list.append(list_left_part[:index_last])
    print(f'coef!!!: {coefficients_list}')
    return coefficients_list

# ДОБАВИТЬ ПУСТЫЕ ЭЛЕМЕНТЫ ПРИ СРАВНЕНИИ СО СПИСКОМ КОЭФФИЦИЕНТОВ


def get_x_polinom_list(pol):
    x_polinom_list = []
    remove_right_part_pol = pol[:-2]
    list_left_part = remove_right_part_pol.split('+')
    for i in range(0, len(list_left_part)):
        try:
            list_left_part[i].index('*')
            index_mult = list_left_part[i].index('*')
            x_el = list_left_part[i][index_mult+1:]
            x_polinom_list.append(x_el)
        except ValueError:
            x_polinom_list.append(list_left_part[i])
    print(f'x!!!: {x_polinom_list}')
    return x_polinom_list


# def check_pol_list(x_list, x_polinom_list, coeff_list):
#     el_x = ''
#     el_coeff = '0'
#     if len(x_list) > len(x_polinom_list):
#         for i in range(0, len(x_list)):
#             try:
#                 if x_polinom_list[i] == x_list[i]:
#                     continue
#                 if x_polinom_list[i].isdigit() == True:
#                     continue
#                 else:
#                     x_polinom_list.insert(i, el_x)
#                     coeff_list.insert(i, el_coeff)
#             except IndexError:
#                 x_polinom_list.insert(i, el_x)
#                 coeff_list.insert(i, el_coeff)
#         print(f'new_x: {x_polinom_list}, new_coeff: {coeff_list}')


print(f'1. {polinom_1}; 2. {polinom_2}')
polynomial_degree_1 = find_polynomial_degree(polinom_1)
polynomial_degree_2 = find_polynomial_degree(polinom_2)
x_list = make_x_list(polynomial_degree_1, polynomial_degree_2)
coeff_list_pol1 = find_coefficients(polinom_1, x_list)
coeff_list_pol2 = find_coefficients(polinom_2, x_list)
x_list_pol1 = get_x_polinom_list(polinom_1)
x_list_pol2 = get_x_polinom_list(polinom_2)
# check_pol_list(x_list, x_list_pol1, coeff_list_pol1)
# check_pol_list(x_list, x_list_pol2, coeff_list_pol2)
