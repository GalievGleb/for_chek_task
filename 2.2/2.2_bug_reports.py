bug_list = ["Ошибка 1 - high",
            "Ошибка 2 - low",
            "Ошибка 3 - medium",
            "Ошибка 4 - critical",
            "Ошибка 5 - low"]
bug_list.append ("Ошибка 6 - high")
priority_order = {
    'critical': 1,
    'high': 2,
    'medium': 3,
    'low': 4
}
bug_list.sort(key=lambda x: priority_order[x.split(" - ")[1]])
filtered_list = []
for bug in bug_list:
    if " - low" not in bug:
        filtered_list.append(bug)
bug_list = filtered_list
print(bug_list)