def get_valid_input():
    while True:
        user_input = input(f"Введите количество тест-кейсов, написанных за сегодня: ")
        if user_input.isdigit():
            num = int(user_input)
            if 0 <= num :
                return num
            else:
                print("Некорректный ввод. Введите положительное число.")
        else:
            print("Вы ввели отрицательное число или вовсе не число. Введите положительное число.")

test_case_quantity = get_valid_input()
if test_case_quantity <= 10:
    print("Попробуйте улучшить результат.")
else:
    print("Отличная работа!")