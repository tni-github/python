def create_list():
    string_text = input('введите список ')
    list_str = list(string_text.split(' '))
    return (list_str)


def is_odd(list_el):
    if int(list_el) % 2 == 0:
        return True
    else:
        return False


def filter_list(list_str):
    filtered_list = list(filter(is_odd, list_str))
    print(filtered_list)


list_str = create_list()
filter_list(list_str)
