def greet_user():
    name = input("Введите ваше имя: ").strip()
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    summa = sum([a, b])
    print(f"Сумма чисел: {summa}")
greet_user()
calculate_sum()