employee_list = ["John Snow", "Piter Pen", "Drakula",
                 "IvanIV", "Moana", "Juilet"]
second = employee_list[1]
second_from_end = employee_list[-2]

print(f"{second}, {second_from_end}")  # работа со списками


def dev_by_three(number):

    if number % 3 == 0:
        return "Да"
    else:
        return "Нет"


number = int(input("Введите число: "))
result = dev_by_three(number)
print(f"Делится ли число {number} на 3? - {result}")  # деление на 3


import math  # noqa: E402

items = int(input("Количество предметов равно: "))


def min_boxes(total_items):
    return math.ceil(total_items / 5)


print(min_boxes(items))  # округление


n = int(input("Введите число: "))


def check_divisibility(n):
    for number in range(1, n + 1):
        if number % 2 == 0 and number % 4 != 0:
            print("Делится на 2, но не на 4")
        elif number % 4 == 0:
            print("Делится и на 2, и на 4")
        else:
            print(number)


check_divisibility(n)  # два делителя


month_number = int(input('Введите номер месяца: '))


def quarter_of_year(month):
    if month in [1, 2, 3]:
        return ('I квартал')
    elif month in [4, 5, 6]:
        return ('II квартал')
    elif month in [7, 8, 9]:
        return ('III квартал')
    else:
        return ('IV квартал')


print(quarter_of_year(month_number))  # квартал


lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

even_numbers = [x for x in lst if x % 3 == 0 and x > 15]

print(even_numbers)  # фильтрация списка


reverse_range = list(range(25, 0, -5))
print(reverse_range)  # range


var_1 = 50
var_2 = 5

print(var_1, var_2)

var_1, var_2 = var_2, var_1

print(var_1, var_2)  # поменять значения местами
