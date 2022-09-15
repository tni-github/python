# 4 - Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифрует его.

import moduleFunc as mod
import os
os.system("cls")


def encrypt(text, key):
    encrypted_text = ''
    mod.enter_number_for_key(key)
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text += ' '
        else:
            encrypted_text += str(chr(ord(text[i])+int(key)))
    with open('encrypt.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)
    return encrypted_text


def decipher():
    deciphered_text = ''
    with open('encrypt.txt', 'r', encoding='utf-8') as file:
        encrypted_text = file.read()
        print(f'Зашифрованный текст: {encrypted_text}')
        key = input(
            'Введите количество символов смещения, которое было использовано при шифровке: ')
        while (int(key) == 0 and int(n) == False):
            key = input('Некорректный ввод. Введите целое число: ')
            return key
        for i in range(0, len(encrypted_text)):
            if encrypted_text[i] == ' ':
                deciphered_text += ' '
            else:
                deciphered_text += str(chr(ord(encrypted_text[i])-int(key)))
        print(f'Расшифрованный текст: {deciphered_text}')
    return deciphered_text


text = input('Введите текст, который нужно зашифровать: ')
step = input('Введите количество символов смещения (например, ввод положительной двойки (2) обозначает сдвиг на 2 символа вправо, ввод отрицательной двойки (-2) - сдвиг на 2 влево: ')
encrypt(text, step)
decipher()
