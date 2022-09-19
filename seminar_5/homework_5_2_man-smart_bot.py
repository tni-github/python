# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет (или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

import os
import moduleFunc as mod
import random
from colorama import init
from colorama import Fore, Back
init()


# очистка консоли
os.system("cls")
# очистка консоли


def check_sum_total():
    print(Fore.BLACK + Back.WHITE)
    n = input('Введите общее количество конфет для игры (не менее 10): ')
    while n.isdigit() == False or int(n) < 10:
        print(Fore.WHITE + Back.RED)
        n = input(
            'Вы ввели некорректное число конфет. Введите целое число не менее 10: ')
    return int(n)


def check_game_move(sum):
    print(Fore.BLACK + Back.WHITE)
    n = input(
        'Введите максимальное число конфет, которое можно брать за один ход игрока (более 1, целое положительное): ')
    while n.isdigit() == False or int(n) <= 1:
        print(Fore.WHITE + Back.RED)
        n = input(
            'Вы указали некорректное число конфет, которое можно брать за один ход. Введите целое число более 1: ')
    while int(n) > int(sum/3):
        print(Fore.WHITE + Back.RED)
        n = input(
            'Вы ввели слишком большое число конфет, которое можно брать за один ход игрока. Введите число поменьше: ')
    return int(n)


def draw_lots(name_1, name_2):
    order_move = ''
    print(Fore.GREEN + Back.CYAN +
          '\nВнимание! Барабанная дробь...Сейчас станет известно, кто ходит первым...')
    k = random.randint(1, 2)
    if k == 1:
        print(Fore.RED + Back.YELLOW + f'\nПервым ходит игрок {name_1}!')
        order_move = name_1
    else:
        print(Fore.YELLOW + Back.RED + f'\nПервым ходит игрок {name_2}!')
        order_move = name_2
    return order_move


def play_game(sum_total, game_move, order_move, name_1, name_2):
    max_sum_after_bot = 0
    while sum_total > 1:
        while order_move == name_1:
            print(Fore.WHITE + Back.GREEN)
            max_sum_after_bot = game_move + 2
            if sum_total >= 2*max_sum_after_bot:
                n = 1
            elif (sum_total - game_move) > game_move:
                n = 1
            elif sum_total == max_sum_after_bot:
                n = 0
                print(Fore.RED + Back.YELLOW +
                      f'Я, {name_1}, наелся и пропущу 1 ход!')
                order_move = name_2
            else:
                if sum_total - 1 > game_move:
                    n = 1
                else:
                    n = sum_total - 1
            if n > 0:
                print(f'{name_1} забирает {n} конфет(-у/-ы).')
            else:
                print(f'{name_1} пропустил ход. Ваша очередь!\n')
            sum_total -= int(n)
            if sum_total == 1:
                return print(Fore.YELLOW + Back.GREEN +
                             f'{name_1} выиграл! Его противнику {name_2} осталась 1 конфета. Поздравляем, {name_1}а')
            if n > 0:
                print(Fore.BLACK + Back.BLUE +
                      f'После хода {name_1}а осталось {sum_total} конфет(-а/-ы)')
            else:
                print(Fore.BLACK + Back.BLUE +
                      f'После пропуска хода {name_1}ом по-прежнему осталось {sum_total} конфет(-а/-ы)')
            order_move = name_2

        while order_move == name_2:
            print(Fore.GREEN + Back.WHITE)
            n = input(
                f'Игрок 2, {name_2}, Ваш ход (должно быть число от 1 до {game_move}): ')
            while n.isdigit() == False or int(n) < 1 or int(n) > game_move:
                print(Fore.WHITE + Back.RED)
                n = input(
                    f'Игрок 2, {name_2}, некорректный ход. Должно быть число от 1 до {game_move}: ')
            sum_total -= int(n)
            if sum_total == 1:
                return print(Fore.YELLOW + Back.GREEN +
                             f'Игрок {name_2}, выиграл! Его противнику {name_1} осталась 1 конфета. Поздравляем, {name_2}!')
            print(Fore.BLACK + Back.BLUE +
                  f'После хода игрока {name_2} осталось {sum_total} конфет(-а)')
            order_move = name_1


sum_total = check_sum_total()
game_move = check_game_move(sum_total)
print(Fore.WHITE + Back.GREEN)
name_1 = 'Bot'
print(f'Привет, я {name_1}. Я буду с тобой играть!')
print(Fore.GREEN + Back.WHITE)
name_2 = input('Игрок № 2, введите Ваше имя: ')
mod.check_for_empty(name_2)
order_move = draw_lots(name_1, name_2)
play_game(sum_total, game_move, order_move, name_1, name_2)
