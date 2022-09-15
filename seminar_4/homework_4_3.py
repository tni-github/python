# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5 //15
# Наталья Тарасова 5 //18
# Фредди Меркури 3 //16
# Денис Байцуров 4 //16  32+18+15=50+15=65 + 3*\т

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

from copy import copy
import os
os.system("cls")


def read_file():
    with open('students.txt', 'r', encoding='utf-8') as file:
        list_students = file.read()
    digit_position = [0]
    list_up = copy(list_students)
    str_num = 0
    for i in range(0, len(list_up)):
        try:
            int(list_up[i])
            digit_position.append(i)
            if int(list_up[i]) > 4:
                for j in range(digit_position[digit_position.index(i)-1]+1, digit_position[digit_position.index(i)]):
                    list_up = list_up.replace(
                        list_up[j], list_up[j].upper())
            else:
                str_num += 1
        except ValueError:
            if list_up[i] == ' ' or list_up[i] == '\n':
                str_num += 1
            else:
                str_num += 1
    return list_up


def write_in_file(list):
    with open('students.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write('-'*25)
        file.write('\n')
        file.write(list)


list_students = read_file()
write_in_file(list_students)
