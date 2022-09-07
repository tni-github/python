# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


print("Программа позволяет понять, является ли день недели выходным")
num_day = input('Введите число от 1 до 7 - порядковый номер дня недели: ')


def is_number(day):
    try:
        int(day)
        return True
    except ValueError:
        return False


def define_day(day):
    while (is_number(day) == False) or (day.isdigit() == True and (int(day) < 1 or int(day) > 7)):
        day = input(
            'Некорректный ввод. Введите целое число от 1 до 7 (вкл.): ')
    else:
        if 1 <= int(day) <= 5:
            print('Надо поработать, это рабочий день')
        else:
            print('Можно отдохнуть, это выходной день')


define_day(num_day)
