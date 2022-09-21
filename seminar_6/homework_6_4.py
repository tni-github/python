# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
import os
os.system("cls")

list_str_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
text_1 = "qwe"

list_str_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
text_2 = "йцу"

list_str_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
text_3 = "йцу"

list_str_4 = ["123", "234", 123, "567"]
text_4 = "123"

list_str_5 = []
text_5 = "123"


list_with_index = list(enumerate(list_str_2))  # меняем список
# print(list_with_index)
list_filtered = list(
    filter(lambda list_with_index: list_with_index[1] == text_2, list_with_index))  # меняем текст, который ищем
index_entrance = list(map(
    lambda list_filtered: list_filtered[0] if len(list_with_index) >= 2 else print(-1), list_filtered))


def result(list):
    try:
        list[1]
        print(list[1])
    except IndexError:
        print(-1)


result(index_entrance)
