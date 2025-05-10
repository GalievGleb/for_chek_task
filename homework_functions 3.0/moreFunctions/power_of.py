def power_of(number, exponent = 2):
    result = number ** exponent
    return result

number = int(input("Введите число: "))
exponent = input("Введите степень (нажмите Enter для квадрата): ")
if exponent:
    exponent = int(exponent)
    result = power_of(number, exponent)
    print(f"Число {number} в степени {exponent} равно {result}.")
else:
    result = power_of(number)  # Используем степень по умолчанию (2)
    print(f"Квадрат числа {number} равен {result}.")