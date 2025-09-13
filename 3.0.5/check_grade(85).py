def check_grade():
    try:
        score = int(input("Введите баллы:"))
    except ValueError:
        print("Введите целое число!")

    if score >= 90:
        print('Отлично')
    elif 89>=score >= 75:
        print("Хорошо")
    elif 74>=score >= 50:
        print("Удовлетворительно")
    else:
        print("Неудовлетворительно")
check_grade()