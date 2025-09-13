import random

# Список возможных приоритетов
priorities = ["High", "Medium", "Low", "Critical", "Blocker"]

# Создаем список баг-репортов случайным образом
bug_reports = []
for i in range(1, 8):
    bug_reports.append(f"Ошибка {i} – {random.choice(priorities)}")

priority = input("Введите приоритет для поиска (High, Medium, Low, Critical, Blocker): ")

filtered_bugs = [bug for bug in bug_reports if priority in bug]

if filtered_bugs:
    print("Найденные баги:")
    for bug in filtered_bugs:
        print(f"- {bug}")
else:
    print("Баги с таким приоритетом не найдены.")
