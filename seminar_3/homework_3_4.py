# 4- Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_decimal_to_binary(num) -> str:
    '''
    Перевод десятичного числа в двоичное
    '''
    while (num.isdigit() == False or float(num) <= 0):
        # проверка на число, целочисленность и на неотрицательность
        num = input(
            'Некорректный ввод. Введите целое положительное число: ')
    else:
        first_num = num
        binary_num = ''
        for i in range(0, len(num)):
            while num != 0:
                binary_num += str(int(num) % 2)
                num = int(int(num)/2)
        return print(f'Десятичное число {first_num} в двоичной системе: {binary_num[::-1]}\u2082')
        # \u2082 - подстрочный индекс "2" (указание на двоичную систему счисления)


n = input('Введите целое положительное число: ')
convert_decimal_to_binary(n)
