def get_valid_input(day):
    while True:
        user_input = input(f"Введите количество тест-кейсов, написанных в {day}: ")
        if user_input.isdigit():
            num = int(user_input)
            if 0 <= num <= 100:
                return num
            else:
                print("Введите корректное значение. Кол-во тест-кейсов должно быть положительным целым числом и не привышать 100.")
        else:
            print("Вы ввели отрицательное число или вовсе не число. Введите корректное значение.")


mon = get_valid_input("пн")
tue = get_valid_input("вт")
wed = get_valid_input("ср")
thu = get_valid_input("чт")
fri = get_valid_input("пт")

work_week = [mon, tue, wed, thu, fri]
print(work_week)

tests_per_week = sum(work_week)
tests_per_day = tests_per_week // 7
print(tests_per_week)
print(tests_per_day)

if tests_per_day <= 10:
    print("Попробуйте улучшить результат.")
else:
    print("Отличная работа!")