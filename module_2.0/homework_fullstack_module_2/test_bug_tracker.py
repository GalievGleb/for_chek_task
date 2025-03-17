qa_info = {'Анна': 3, 'Иван': 5, 'Дмитрий': 7}

qa = input("Введите имя тестировщика: ")
qa = qa.capitalize()
if qa in qa_info:
    qa_info[qa] += 1
else:
    qa_info[qa] = 1
print(f'Обновленные данные: {qa_info}')