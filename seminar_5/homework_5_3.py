# 3-Создайте два списка — один с названиями языков программирования,
# другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
#
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и
# языка, написанного большими буквами: [(1,'PYTHON'), (2,'C#')]

# Вторая — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет:
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров
# букв в слове. Порядковые номера смотрите в этой таблице,
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

from typing import List, Optional
import os  # импорт библиотеки для очистки консоли
from colorama import init
from colorama import Fore, Back
init()

# очистка консоли
os.system("cls")
# очистка консоли

list_num = []
list_tuples = []
new_list_tuples = []
new_list_tuples_finall = []
new_tuple_elem = tuple()
list_capital_letters = []
list_before_replacing = []
list_prog_lang = ['javascript', 'python', 'c#', 'java', 'php', 'c++', 'go']


def make_num_list(list_str: Optional[str]) -> List[int]:
    '''
    Функция составляет списокс с целыми положительными числами
    от 1 до длины другого списка со строковыми значениями.
    '''
    for i in range(1, len(list_str)+1):
        list_num.append(i)
    return list_num


def make_list_with_tuples(list_num: int, list_str: str):
    '''
    Функция составляет кортеж из двух совмещенных поэлементно списков и возвращает его.
    '''
    list_capital_letters = list(map(lambda word: word.upper(), list_str))
    list_tuples = list(zip(list_num, list_capital_letters))
    return list_tuples


def find_sum_of_points(text_str: Optional[str]) -> Optional[int]:
    '''
    Функция находит сумму очков по принимаемому тексту.
    Суммой очков называется сложение порядковых номеров букв в слове. П
    орядковые номера смотрите в этой таблице, в третьем столбце: 
    https://www.charset.org/utf-8
    '''
    sum_of_points = 0
    for i in range(0, len(text_str)):
        sum_of_points += int(ord(text_str[i]))
    return sum_of_points


def is_necessary_elem(elem: Optional[tuple]) -> Optional[bool]:
    '''
    Функция проверяет, имеет ли сумма очков слова 
    внутри кортежа в делителях номер, с которым это слово в паре в кортеже. 
    Возвращает True - если имеет, False - если нет.
    '''
    sum_of_points = find_sum_of_points(elem[1])
    if sum_of_points % elem[0] == 0:
        return True
    else:
        return False


def make_new_tuples_list(list_tuples: List[tuple]) -> List[tuple]:
    '''
    Функция составляет итоговый список кортежей, отфильтровав исходный список 
    следующим образом:
    если сумма очков слова имеет в делителях номер,
    с которым она в паре в кортеже,
    то кортеж остается, его номер заменяется на сумму очков.
    Если нет — удаляется.
    '''
    sum = 0
    new_list_tuples = list(
        filter(is_necessary_elem, list_tuples))
    for i in range(0, len(new_list_tuples)):
        sum_of_points = find_sum_of_points(new_list_tuples[i][1])
        sum += sum_of_points
        list_before_replacing = list(new_list_tuples[i])
        list_before_replacing[0] = sum_of_points
        new_list_tuples_finall.append(tuple(list_before_replacing))
    return [new_list_tuples_finall, sum]


list_num = make_num_list(list_prog_lang)
list_tuples = make_list_with_tuples(list_num, list_prog_lang)
new_filtered_replaced_list = make_new_tuples_list(list_tuples)

print(Fore.MAGENTA + Back.BLUE +
      f'Исходный совмещенных из список {list_tuples} преобразован в список {new_filtered_replaced_list[0]}, сумма чисел из нового списка кортежей равна {new_filtered_replaced_list[1]}.')
