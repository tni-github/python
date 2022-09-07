# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково,
# но есть одно "но".
# если перевернутое число не равно исходному,
# то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.
num_digits = 0


def find_palindrom(number):
    while (number.isdigit() == False or float(number) <= 0 or int(number) == 196):
        # проверка на число, целочисленность и на положительность
        number = input(
            'Некорректный ввод. Введите целое положительное число (кроме 196): ')
    else:
        num_digits = len(number)
        first_number = int(number)
        reversed_number = 0
        for i in range(1, int(num_digits)+1):
            additional_number = int(int(number)/(10**(i-1)))
            reversed_digit = (additional_number % 10) * \
                (10**(int(num_digits)-i))
            reversed_number += int(reversed_digit)

        if int(number) == reversed_number:
            return print(f'Число "{number}" является палиндромом (само по себе)')
        else:
            step = 0
            while int(number) != reversed_number:
                step += 1
                number = int(number) + reversed_number
                num_digits = len(str(number))
                reversed_number = 0
                for i in range(1, int(num_digits) + 1):
                    additional_number = int(int(number)/(10**(i-1)))
                    reversed_digit = (additional_number %
                                      10) * (10**(int(num_digits)-i))
                    reversed_number += int(reversed_digit)
            else:
                return print(
                    f'Число "{reversed_number}" является палиндромом числа "{first_number}" {step}-й ступени')


print('ВАЖНО: не указывайте число "196", поскольку это число, к которому палиндром не будет найден, даже при огромном числе операций!')
number = input(
    'Введите целое положительное число для нахождения его палиндрома: ')
find_palindrom(number)
