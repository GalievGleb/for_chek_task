def is_even(number):
    return "чётным" if number % 2 == 0 else "нечётным"

number = int(input("Введите число: "))
print(f"Число {number} является {is_even(number)}.")

