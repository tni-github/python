# 2-Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

def truth_table():
    n_table = ' '*5+'|'+' '*5
    n_header = '-'*50
    print(n_header)
    print(f'|    X{n_table}Y{n_table}Z{n_table}Result  |', sep='\n')
    print(n_header)
    for X in range(0, 2):
        for Y in range(0, 2):
            for Z in range(0, 2):
                result = not (X or Y or Z) == (not (X) and not (Y) and not (Z))
                print(
                    f'|    {X}{n_table}{Y}{n_table}{Z}{n_table}{result}    |')
                print(n_header)


truth_table()
