# 2 - Напишите программу, которая принимает на вход число N и выдает
# набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def count_factorial(num):
    while (num.isdigit() == False or float(num) < 0):
        # проверка на число, целочисленность и на неотрицательность
        num = input(
            'Некорректный ввод. Введите целое положительное число или ноль: ')
    else:
        factorial_value = 1
        factorial_arr = []
        if int(num) == 0:
            factorial_value = 1
            factorial_arr.append(factorial_value)
        else:
            for i in range(1, int(num) + 1):
                factorial_value *= i
                factorial_arr.append(factorial_value)
    print(
        f'Факториал числа {num} равен {factorial_value}: {num}! = {factorial_value}')
    print(
        f'Последовательный набор произведений при вычислении факториала: {factorial_arr}')


number = input('Введите целое число, факториал которого нужно найти: ')
count_factorial(number)
