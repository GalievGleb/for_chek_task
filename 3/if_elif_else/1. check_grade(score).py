def check_grade(score):
    if 90 <= score <= 100:
        grade="Отлично"
    elif 75 <= score <= 89:
        grade="Хорошо"
    elif 50 <= score <= 74:
        grade="Удовлетворительно"
    else:
        grade="Неудовлетворительно"
    return grade

score = 85

result = check_grade(score)

print(f"Оценка за {score} баллов: {result}")