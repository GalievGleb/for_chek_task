# Задача 1: Оценка по шкале
def check_grade(score):
    if score >= 90 and score <= 100:
        return "Отлично"
    elif score >= 75 and score <= 89:
        return "Хорошо"
    elif score >= 50 and score <= 74:
        return "Удовлетворительно"
    elif score >= 0 and score <= 50:
        return "Неудовлетворительно"
    else:
        return "ошибка"
score = 185
print(f"Оценка за {score} баллов: {check_grade(score)}.")



