
mondey=int(input("Сколько тест-кейсов было написано в понедельник?: "))
tuesday=int(input("Сколько тест-кейсов было написано во вторник?: "))
wednesday=int(input("Сколько тест-кейсов было написано в среду?: "))
thursday=int(input("Сколько тест-кейсов было написано в четверг?: "))
friday=int(input("Сколько тест-кейсов было написано в пятницу?: "))
saturday=int(input("Сколько тест-кейсов было написано в субботу?: "))
sunday=int(input("Сколько тест-кейсов было написано в воскресенье?: "))

summ=mondey+tuesday+wednesday+thursday+friday+saturday+sunday
print(f"Общее кол-во тестов за неделю {summ}")
ave=round(summ/7)
print(f"Среднее кол-во тестов в день {ave}")
if ave > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")

