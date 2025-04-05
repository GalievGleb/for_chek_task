bug_list=["Ошибка 1 - High", "Ошибка 2 - Low", "Ошибка 3 - Middle", "Ошибка 4 - High", "Ошибка 5 - Low"]

print(f"Список баг репортов: \n {bug_list}")


while True:
    update=(input("Что хотите сделать со списком?"
             "\nДействие                           Команда"
             "\nДобавить новый баг                 upd"
             "\nУдалить баг с низким приоритетом   del"
             "\nСортировать баги по приоритету     sor"
             "\nВыйти из программы                 exit"
             "\nВведите команду: "))

    if update == "upd":
        bug_list.append(input("Введите новый баг репорт в формате 'Ошибка N - High' где N это номер ошибки, а High серьезность: "))
        print(f"Пополненный список: \n{bug_list}")

    elif update == "del":
        bug_list = [bug for bug in bug_list if "Low" not in bug]
        print(f"Список после удаления багов с низким приоритетом: \n{bug_list}")

    elif update == "sor":
        priority_order = {"High": 1, "Middle": 2, "Low": 3}
        bug_list.sort(key=lambda bug: priority_order[bug.split(" - ")[1]])
        print(f"Отсортированный список: \n{bug_list}")

    elif update == "exit":
        break

    else:
        print("Команда не распознана.")