testers_bugs = ({'Анна': 3, 'Иван': 5, 'Дмитрий': 7})
print("Исходные данные:", testers_bugs)
while True:
    tester_name = input("Введите имя тестировщика: ").strip().capitalize()
    if tester_name:
        break
    print("Ошибка: имя не может быть пустым. Попробуйте снова.")
if tester_name in testers_bugs:
    testers_bugs[tester_name] += 1
else:
    testers_bugs[tester_name] = 1
print("Обновленные данные:", testers_bugs)
