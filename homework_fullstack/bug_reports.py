
bug_reports = ["Ошибка 1 - High", "Ошибка 2 - Low", "Ошибка 3 - High", "Ошибка 4 - Low", "Ошибка 5 - Medium"]
def add_bug_report(report):
    bug_reports.append(report)
    print(f"Баг добавлен: {report}")

def delete_low_priority_bugs():
    for report in bug_reports:
        if "Low" in report:
            bug_reports.remove(report)
            print(f"Баг удален: {report}")
            return

def sort_bugs():
    priority={"High": 1, "Medium": 2, "Low": 3}
    bug_reports.sort(key=lambda x: priority[x.split(" - ")[1]])
    print("Баги отсортированы по приоритету")

if __name__ == "__main__":

 # Печать текущего списка багов
    print("Текущий список багов:")
    for bug in bug_reports:
        print(bug)

    add_bug_report("Ошибка 6 - Low")
    delete_low_priority_bugs()
    sort_bugs()
    print(bug_reports)







