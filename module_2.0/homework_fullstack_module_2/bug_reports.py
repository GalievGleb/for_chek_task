import re

bugs_reports = ['Ошибка 1 — Critical', 'Ошибка 2 — Low', 'Ошибка 3 — Critical', 'Ошибка 4 — Low', 'Ошибка 5 — Critical']
priority = {
    'Critical': 1,
    'Low': 2
}

def add_bug():
    new_bug = input('Заведите баг по шаблону: <Ошибка <номер> — <приоритет>.\nВарианты приоритета: Low, Critical\n')
    pattern = r"Ошибка \d+ — (Low|Critical)"

    if re.match(pattern, new_bug):
        bugs_reports.append(new_bug)
        print('Баг добавлен!')
        return bugs_reports
    else:
        print('Неправильный формат.')
        return None

def get_priority(bug):
    priority_level = bug.split(' — ')[-1]
    return priority[priority_level]

def sort_bugs_reports(bugs_reports):
    bugs_reports.sort(key=get_priority)

def delete_low_priority_bugs(bugs_reports):
    for i in range(len(bugs_reports) - 1, -1, -1):
        if 'Low' in bugs_reports[i]:
            del bugs_reports[i]
        else:
            break

add_bug()
print(bugs_reports)
sort_bugs_reports(bugs_reports)
print(bugs_reports)
delete_low_priority_bugs(bugs_reports)
print(bugs_reports)


