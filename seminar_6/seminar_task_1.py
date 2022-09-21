# Напишите программу вычисления арифметического выражения,
# заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок,
# меняющих приоритет операций
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;

# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# (256 - 194 => некорректная запись скобок

# import re
import sys
from colorama import Fore, Back
from colorama import init
import os
import moduleFunc as mod
init()

# очистка консоли
os.system("cls")
# очистка консоли

text = '-501  + 358'

operations = ['+', '-', '/', '*']
list_symbols = []
list_with_nums = []


def check_string(string_expression):
    string_expression = mod.remove_spaces_in_string(string_expression)
    # вычищаем пробелы из строки
    # print(string_expression)
    if string_expression[len(string_expression)-1] in operations:
        print(Fore.CYAN + Back.RED +
              f'\nНедостаточно числовых данных. Выражение "{string_expression}" обрывается на знаке, а должно заканчиваться числом')
        sys.exit()
    for i in range(0, len(string_expression)):
        if string_expression[i].isalpha():
            print(Fore.CYAN + Back.RED +
                  f'\nНеправильный ввод: нужны числа. Выражение "{string_expression}" содержит букву(-ы)')
            sys.exit()
        else:
            continue
    list_numbers = []
    count = 0
    temp_num = ''
    while count < len(string_expression) and string_expression[count].isdigit():
        temp_num += string_expression[count]
        count += 1
    list_numbers.append(temp_num)
    # list_number.append(string_expression[count])
    # count += 1
    print(list_numbers)
    # print(list_with_nums)


check_string(text)

# while len(text) == 0 or re.search(r'\S', text) == None:
#         text = input('Вы ничего не ввели. Попробуйте снова: ')
# re.search(r'[0-9]', list_symbols[j]).group(0)
