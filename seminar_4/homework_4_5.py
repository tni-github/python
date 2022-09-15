# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

import os
from re import S
os.system("cls")

compressed_list = []


def read_file_with_regular():
    with open('regular_text.txt', 'r', encoding='utf-8') as file:
        regular_text = file.read()
        return regular_text


def read_file_with_compression():
    with open('compressed_text.txt', 'r', encoding='utf-8') as file:
        compressed_text = file.read()
        return compressed_text


def compress_text(text):
    counter = 1
    compressed_text = ''
    space_num = 0
    new_line_num = 0
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        if text[i] != text[i-1]:
            compressed_list.append(counter)
            compressed_list.append(text[i-1])
            if i == len(text) - 1:
                counter = 1
                compressed_list.append(counter)
                compressed_list.append(text[i])
            counter = 1
            continue
    for i in range(0, len(compressed_list)):
        if compressed_list[i] == ' ':
            space_num += 1
        if compressed_list[i] == '\n':
            new_line_num += 1
    for i in range(0, len(compressed_list) - space_num - new_line_num):
        if compressed_list[i] == 1 and (compressed_list[i+1] == ' ' or compressed_list[i+1] == '\n'):
            del compressed_list[i]
    for i in range(0, len(compressed_list)):
        if (type(compressed_list[i])) == int:
            compressed_list[i] = str(compressed_list[i])
        compressed_text += compressed_list[i]
    return compressed_text

# 12A11B10C6D5E4F1G 1p1y1t1h1o1n 1i1s 1s7o 1c7o1l


words = []
numbers = []


def decompress_text(text):
    decompessed_text = ''
    words = "".join(" " if el.isdigit() else el for el in text).split()
    numbers_first = "".join(el if el.isdigit() else " " for el in text).split()
    numbers = numbers_first.copy()
    for i in range(0, len(numbers)):
        if words[i] == ' ':
            decompessed_text += ' '
        if words[i] == '\n':
            decompessed_text += '\n'
        else:
            numbers[i] = int(numbers[i])
            while numbers[i] > 0:
                decompessed_text += words[i]
                numbers[i] -= 1
    return decompessed_text


def write_in_file_with_compression(string_text):
    with open('compressed_text.txt', 'w', encoding='utf-8') as file:
        file.write(string_text)


def write_in_file_with_regular(string_text):
    with open('regular_text.txt', 'w', encoding='utf-8') as file:
        file.write(string_text)


# следующие 2 строки для сжатия текста
regular_text = read_file_with_regular()
write_in_file_with_compression(compress_text(regular_text))

# следующие 2 строки для восстановления данных
# compressed_text = read_file_with_compression()
# write_in_file_with_regular(decompress_text(compressed_text))
