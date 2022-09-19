# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

from typing import List, Optional
from colorama import Fore, Back
import os
import re
import moduleFunc as mod
from colorama import init
init()


# очистка консоли
os.system("cls")
# очистка консоли


def check_for_empty(text: Optional[str]):
    '''
    Функция проверяет строку на пустоту или пробел(-ы) и зацикливает ввод текста
    до появления каких-либо других символов.
    '''
    while len(text) == 0 or re.search(r'\S', text) == None:
        text = input('Вы ничего не ввели. Попробуйте снова: ')


def divide_string_to_list(text: Optional[str]) -> List:
    '''
    Функция разделяет строку на список.
    '''
    list_from_text = mod.divide_string_to_list(text)
    return list_from_text


def check_word(word: Optional[str]) -> Optional[bool]:
    '''
    Функция проверяет принимаемое слово: есть ли внутри символы "абв", либо
    равно ли данное слово "абв". ВАЖНО: если проверка проходит с положительным
    итогом проверки (слово содержит"абв"), функция возвращает False, в обратном случае - True.
    '''
    if 'абв' in word or word == 'абв':
        return False
    else:
        return True


def change_text():
    '''
    Функция удаляет из текста все слова, содержащие "абв".
    '''
    print(Fore.BLACK + Back.GREEN +
          'Программа удаляет из текста, введенного пользователем, слова, содержащие "абв"', sep='\n')
    text = input('\nВведите первоначальный текст (в свободной форме): ')
    check_for_empty(text)
    list_from_text = divide_string_to_list(text)
    new_text_list = list(filter(check_word, list_from_text))
    new_text = ' '.join(new_text_list)
    if len(text) == len(new_text):
        print(Fore.RED + Back.YELLOW +
              f'\nВ первоначальном тексте "{text}" нет ни одного слова, содержащего "абв"!')
    else:
        print(
            Fore.BLUE + Back.CYAN + f'\nИз первоначальной строки "{text}" путем удаления слов, содержащих "абв", получена новая строка: "{new_text}"\n')
    return new_text


change_text()
