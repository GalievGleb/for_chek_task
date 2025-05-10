import random

def create_bug_report():
    priorities = ['High', 'Medium', 'Low']
    for i in range(7):
        priority = random.choice(priorities)
        bug_reports.append(f'Ошибка {i+1} - {priority}')
    return bug_reports

def bug_filter(bug_reports):
    priorities = ['High', 'Medium', 'Low']
    while True:
        user_input = input(f"Введите интересующий вас приоритет High / Medium / Low: ")
        if user_input in priorities:
            for bug in bug_reports:
                if user_input in bug:
                    print(bug)
            break
        else:
            print("Некорректный ввод. Введите High / Medium / Low.")


bug_reports = []
create_bug_report()
print(bug_reports)
bug_filter(bug_reports)


