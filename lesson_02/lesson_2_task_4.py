n = int(input('Введите целое число: '))


def fizz_buzz(n):
    for number in range(1, n + 1):
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)


fizz_buzz(n)
