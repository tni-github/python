# Создайте программу для игры в ""Крестики-нолики"".

import random
import sys
import moduleFunc as mod
from typing import List, Optional
from colorama import init
from colorama import Fore, Back
import os

# очистка консоли
os.system("cls")
# очистка консоли
init()

print(Fore.RED + Back.YELLOW + 'Игра "Крестики-нолики".')
print(Fore.RED + Back.WHITE + '\nПравила игры:\nИгроки по очереди ставят на свободные клетки поля 3х3 знаки\n(один всегда крестики, другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.\nИгрок, который ходит, первым, определяется случайным образом.\nКто ходит первым - ставит крестики.')

num_row = 3
result = False


def create_num_list(n: Optional[int]) -> List[int]:
    '''
    Программа создает список с номерами игровых клеток, начиная с единицы.
    '''
    list_num = []
    for i in range(1, n**2+1):
        list_num.append(i)
    return list_num


def create_playing_field(list_num: Optional[List], num_row):
    '''
    Функция отрисовывает игровое поле.
    '''
    symbol_space = ' '
    symbol_line = '-'
    num_base = 9
    print(Fore.RED + Back.WHITE + '\nИгровое поле:\n')
    for i in [0, 3, 6]:
        print(f'{symbol_line*num_base*num_row}', sep='\n\n')

        print(
            f'|{symbol_space*(num_base-2)}|{symbol_space*(num_base-1)}|{symbol_space*(num_base-2)}|')

        print(
            f'|{symbol_space*3}{list_num[i]}{symbol_space*3}|{symbol_space*4}{list_num[i+1]}{symbol_space*3}|{symbol_space*3}{list_num[i+2]}{symbol_space*3}|')

        print(
            f'|{symbol_space*(num_base-2)}|{symbol_space*(num_base-1)}|{symbol_space*(num_base-2)}|')
        if i == 6:
            print(f'{symbol_line*num_base*num_row}', sep='\n')


def draw_lots(name_1: Optional[str], name_2: Optional[str]) -> Optional[List]:
    '''
    Функция случайного определения игрока, который ходит первым.
    '''
    players = []
    print(Fore.RED + Back.WHITE +
          '\nВнимание! Барабанная дробь... Сейчас станет известно, кто ходит первым... Итак, жребий выпал...')
    k = random.randint(1, 2)
    if k == 1:
        print(
            f'Первым ходит игрок {name_1} - будете ставить крестики. Игрок {name_2} ставит нолики.')
        players.append((name_1, 'Х'))
        players.append((name_2, 'O'))
    if k == 2:
        print(Fore.RED + Back.WHITE +
              f'Первым ходит игрок {name_2}! Будете ставить крестики. Игрок {name_1} ставит нолики. ')
        players.append((name_1, 'O'))
        players.append((name_2, 'X'))
    return players


def get_first_move_player(players: Optional[List]) -> Optional[str]:
    '''
    Функция опеределяет игрока, ходящего первым.
    '''
    first_move = ''
    for i in range(0, len(players)):
        if players[i][1] == 'Х':
            first_move = players[i][0]
    return first_move


def check_for_draw(list_num_field, result):
    '''
    Функция проверяет наличие не заполненных крестиком или ноликом клеток,
    чтобы избежать ситуации когда никто не выиграл и при этом поле больше нельзя ничем заполнять.
    '''
    num = 0
    for i in range(0, len(list_num_field)):
        try:
            int(list_num_field[i])
            num += 1
        except ValueError:
            continue
    if num == 0 and result != 1:
        result = 1
        print(Fore.CYAN + Back.GREEN +
              'В игре ничья! Никто не выиграл и никто не проиграл')
        sys.exit()


def check_result(list_num_field: Optional[List], sign) -> Optional[int]:
    '''
    Функция проверяет, есть ли на игровом поле выигрышная комбинация
    (строка / столбец / диагональ с одинаковыми элементами).
    '''
    result = 0
    for i in [0, 3, 6]:
        if list_num_field[i] == sign and list_num_field[i+1] == sign and list_num_field[i+2] == sign:
            result = 1
    for i in [0, 1, 2]:
        if list_num_field[i] == sign and list_num_field[i+3] == sign and list_num_field[i+6] == sign:
            result = 1
    if i == 0:
        if list_num_field[i] == sign and list_num_field[i+4] == sign and list_num_field[i+8] == sign:
            result = 1
    if i == 2:
        if list_num_field[i] == sign and list_num_field[i+2] == sign and list_num_field[i+4] == sign:
            result = 1
    return result


def play_game(players: Optional[List], list_num_field: Optional[List], first_move: Optional[str], name_1: Optional[str], name_2: Optional[str], num_row: Optional[int]):
    '''
    Функция определяет процесс игры: ходы игроков, отрисовка нового игрового поля
    (с учетом сделанных ходов), проверка на выигрыш и на ничью.
    '''
    result = 0
    print(Fore.CYAN + Back.LIGHTBLUE_EX)
    while result != 1:
        check_for_draw(list_num_field, result)
        while first_move == name_1:
            print(Fore.CYAN + Back.LIGHTBLUE_EX)
            step = input(
                f'\nИгрок {name_1}, Ваш ход. Укажите номер на поле, куда поставите {players[0][1]}: ')
            try:
                list_num_field.index(int(step))
                if list_num_field.index(int(step)) >= 0:
                    index_step = list_num_field.index(int(step))
                    list_num_field[index_step] = players[0][1]
                    create_playing_field(list_num_field, num_row)
                    result = check_result(list_num_field, players[0][1])
                    check_for_draw(list_num_field, result)
                if result == 1:
                    return print(Fore.LIGHTYELLOW_EX + Back.GREEN +
                                 f'{first_move}, поздравляем, Вы выиграли!!!')
                first_move = name_2
            except ValueError:
                print(Fore.GREEN + Back.RED +
                      f'Введено некорректное значение (либо поставлен лишний символ, либо клетка занята, либо ее нет на игровом поле)')
        while first_move != name_1:
            print(Fore.CYAN + Back.LIGHTBLUE_EX)
            step = input(
                f'\nИгрок {name_2}, Ваш ход. Укажите номер на поле, куда поставите {players[1][1]}: ')
            try:
                list_num_field.index(int(step))
                if list_num_field.index(int(step)) >= 0:
                    index_step = list_num_field.index(int(step))
                    list_num_field[index_step] = players[1][1]
                    create_playing_field(list_num_field, num_row)
                    result = check_result(list_num_field, players[1][1])
                    check_for_draw(list_num_field, result)
                if result == 1:
                    return print(Fore.LIGHTYELLOW_EX + Back.GREEN +
                                 f'{first_move}, поздравляем, Вы выиграли!!!')
                first_move = name_1
            except ValueError:
                check_for_draw(list_num_field, result)
                print(Fore.GREEN + Back.RED +
                      f'Введено некорректное значение (либо поставлен лишний символ, либо клетка занята, либо ее нет на игровом поле)')


list_num_field = create_num_list(num_row)
create_playing_field(list_num_field, num_row)
print(Fore.CYAN + Back.LIGHTBLUE_EX)
name_1 = input('Игрок № 1, введите Ваше имя: ')
name_1 = mod.check_for_empty(name_1)
name_2 = input('\nИгрок № 2, введите Ваше имя: ')
name_2 = mod.check_for_empty(name_2)
players = draw_lots(name_1, name_2)
first_move = get_first_move_player(players)
play_game(players, list_num_field, first_move, name_1, name_2, num_row)
