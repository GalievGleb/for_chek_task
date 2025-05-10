mon=int(input("Добрый день, сколько тест-кейсов выполнил в понедельник?: "))
tue=int(input("А во вторник?: "))
wed=int(input("А в среду?: "))
thu=int(input("А в четверг?: "))
fri=int(input("А в пятницу?: "))

all_test_case=mon+tue+wed+thu+fri
average=(mon+tue+wed+thu+fri)//5

print(f"Общее число выполненных тест-кейсов: {all_test_case}")
print(f"Среднее число тест кейсов: {average}")

if average > 10:
    print("Отличная работа! Так держать")
else:
    print("Попробуй улучшить результат!")
