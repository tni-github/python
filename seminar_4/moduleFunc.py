from tokenize import Number
from xmlrpc.client import Boolean


def enter_natural_number(n: int) -> int:
    '''
    Проверка числа: является ли оно натуральным, зацикливание ввода числа, если не является
    '''
    while (n.isdigit() == False or int(n) <= 0):
        n = input('Некорректный ввод. Введите натуральное число: ')
    return n


def enter_number(n: Number) -> Number:
    '''
    Проверка на ввод числа
    '''
    while (n.isdigit() == False or float(n) == False):
        n = input('Некорректный ввод. Введите число: ')
    return n


def enter_number_for_key(n: int) -> int:
    '''
    Проверка на ввод целого числа и не равного нулю
    '''
    while (int(n) == 0 and int(n) == False):
        n = input('Некорректный ввод. Введите целое число: ')
    return n


def find_factorial(n: int) -> int:
    '''
    Поиск факториала числа
    '''
    factorial = 1
    if int(n) == 0 or int(n) == 1:
        factorial = 1
    elif int(n) == 2:
        factorial = 2
    else:
        for i in range(2, int(n) + 1):
            factorial *= i
    return factorial


# Согласно теореме Вильсона, если n — простое число, то
# [(n–1)! + 1] делится на n (без остатка), что заложено в основу следующей функции check_is_prime_number(n)
def check_is_prime_number(n: int) -> Boolean:
    '''
    Проверка числа: является ли оно простым
    '''
    n_prev = int(n) - 1
    factorial_n_prev = find_factorial(n_prev)
    if (factorial_n_prev + 1) % int(n) == 0:
        return True
    else:
        return False


def make_prime_number_list(n: int) -> list:
    '''
    Составляет список простых чисел в интервале от 1 до числа n
    '''
    prime_number_list = []
    for i in range(1, int(n)+1):
        if check_is_prime_number(i) == True:
            prime_number_list.append(i)
    return prime_number_list


def null_counter(num: float):
    '''
    Переносит точку в числе и считает, сколько знаков после точки
    param: num - вещественное число
    return: counter - количество символов после точки, num = int
    '''
    counter = 0
    while num != int(num):
        num *= 10
        counter += 1
    return counter


def get_str_quantity(list: list) -> int:
    '''
    Вычисляет количество строковых значений в списке
    '''
    str_quantity = 0
    for i in range(0, len(list)):
        if type(list[i]) == str:
            str_quantity += 1
    return str_quantity


def clear_list(list: list, k: int) -> list:
    '''
    Чистит список: при наличии в нем строковых значений удаляет их из списка
    '''
    for i in range(0, len(list) - k + 1):
        if type(list[i]) == str:
            del list[i]
    return list
