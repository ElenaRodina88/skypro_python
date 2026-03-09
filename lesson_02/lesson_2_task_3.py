import math

side = float(input('Введите сторону квадрата: '))


def square(square_side):
    return math.ceil(square_side * square_side)


print(square(side))
