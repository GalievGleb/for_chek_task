def is_even(number):
    result = 'Четное' if number % 2 == 0 else 'Нечетное'
    print(result)


number = int(input('Введите число:'))
is_even(number)
