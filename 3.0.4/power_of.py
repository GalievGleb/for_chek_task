def power_of():
    while True:
        try:
            num = float(input("Введите число: "))
            break  # Выход из цикла, если ввод корректен
        except ValueError:
            print("Ошибка: Введите корректное число.")

    while True:
        expo = input("Введите степень (оставьте пустым для квадрата): ")
        if expo == '':
            expo = 2  # Используем значение по умолчанию
            result = num ** expo
            print(f'Число {num} в квадрате равно {result}')
            break  # Выход из цикла
        else:
            try:
                expo = int(expo)  # Преобразуем ввод в целое число
                result = num ** expo
                print(f'Число {num} в степени {expo} равно {result}')
                break  # Выход из цикла
            except ValueError:
                print("Ошибка: Введите корректную степень.")
# Вызов функции
power_of()