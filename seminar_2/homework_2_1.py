# 1 - Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример: 67.82 -> 23; 0.56 -> 11


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def number_decimal_places(num):
    first_num = num
    while is_number(num) == False:
        # проверка на число
        num = input(
            'Некорректный ввод (не число). Введите число (дробная часть от целой отделяется точкой): ')
    else:
        if float(num) < 0:
            num = abs(float(num))
        num_str = str(num)
        num_list = list(num_str)
        sum = 0
        for i in range(0, len(num_str)):
            if (num_list[i] != '.'):
                sum += int(num_list[i])
        return print(f'Сумма цифр числа {first_num} равняется {sum}')


number = input(
    'Введите число, для которого будет сделан подсчет суммы его цифр (дробная часть от целой отделяется точкой): ')
number_decimal_places(number)
