def find_max(a, b):
    if a > b:
        return f"Максимальное из чисел {a} и {b}: {a}"
    else:
        return f"Максимальное из чисел {a} и {b}: {b}"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(find_max(num1, num2))

