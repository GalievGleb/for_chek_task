name = input('Введите ваше имя: ').capitalize()

def greet_user(name):
    print(f'Привет, {name}! Добро пожаловать в мир Python!')

greet_user(name)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def calculate_sum(a, b):
    sum = a + b
    print(f'Сумма чисел: {sum}')

calculate_sum(a, b)
