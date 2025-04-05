def greet_user(name):
    return print(f"Привет {name}, добро пожаловать в мир Python!")

def calculate_sum(a, b):
    sum = a + b
    return print(f"Сумма равна {sum}")

name_user = input("Введите ваше имя: ")

greet_user(name_user)

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))

calculate_sum(num_a, num_b)