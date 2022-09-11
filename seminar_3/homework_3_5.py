# 5-Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://clck.ru/yWbkX.)

def fibonacci_negafibonacci(k):
    fibonacci_list = [0, 1]
    negafibonacci_list = []
    negafibonacci_reversed = []
    fibonacci_full = []
    while (k.isdigit() == False or float(k) <= 0):
        # проверка на число, целочисленность и на неотрицательность
        k = input(
            'Некорректный ввод. Введите целое положительное число: ')
    else:
        for i in range(2, int(k)+1):
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
        print(fibonacci_list)
        # получаем список Фибоначчи
        for i in range(1, len(fibonacci_list)):
            negafibonacci_list.append((-1)**(i+1)*fibonacci_list[i])
            # получаем список Негафибоначчи
        for i in range(0, len(negafibonacci_list)):
            negafibonacci_reversed.append(
                negafibonacci_list[len(negafibonacci_list)-i-1])
            # переворачиваем массив Негафибоначчи,
            # чтобы при совмещении был правильный порядок
        fibonacci_full = negafibonacci_reversed.copy() + fibonacci_list.copy()
        # совмещаем оба списка для получения общего
        print(fibonacci_full)


k = input(
    'Введите количество чисел Фибоначчи (должно быть целое положительное число): ')
fibonacci_negafibonacci(k)
