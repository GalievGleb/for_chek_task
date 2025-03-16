while True:
    user_input = input("Введите количество тест-кейсов, которые вы выполнили за день: ")

    if user_input.isdigit() and int(user_input) > 0:
        test_cases = int(user_input)
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите положительное целое число.")

if test_cases > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
