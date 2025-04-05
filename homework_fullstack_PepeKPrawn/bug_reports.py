bug_reports = [
    "Ошибка 1 — High",
    "Ошибка 2 — Low",
    "Ошибка 3 — Major",
    "Ошибка 4 — High",
    "Ошибка 5 — Low"
]
def remove_low_bugs():
    global bug_reports
    i = 0
    while i < len(bug_reports):
        if "Low" in bug_reports[i]:
            print(f"Баг удален: {bug_reports[i]}")
            bug_reports.pop(i)
        else:
            i += 1
    if not any("Low" in bug for bug in bug_reports):
        print("Нет багов с низким приоритетом.")

def add_bug():
    global bug_reports
    new_bug = input("Введите описание нового бага в формате:'Ошибка n - priotity'")
    bug_reports.append(new_bug)
    print(f"Баг '{new_bug}' добавлен.")
def sort_bugs():
    global bug_reports
    priority_order = {'Low': 1, 'Major': 2, 'High': 3, 'Blocker': 4}
    bug_reports.sort(key=lambda x: priority_order.get(x.split("—")[-1].strip(), 0), reverse=True)
    print("Баги отсортированы по приоритету.")
print("Изначальный список багов:")
print(bug_reports)

remove_low_bugs()
add_bug()
sort_bugs()
print("\nИтоговый список багов:")
print(bug_reports)