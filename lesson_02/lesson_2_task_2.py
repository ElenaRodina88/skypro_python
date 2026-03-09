def is_year_leap(number):
    if number % 4 == 0:
        return True
    else:
        return False


number = int(input('Введите год: '))
result = is_year_leap(number)

print(f'год {number} : {result}')
