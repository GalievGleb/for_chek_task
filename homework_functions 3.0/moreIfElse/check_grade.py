def check_grade(score):
    if 100 >= score >=90:
        return f"Оценка за {score} баллов: Отлично."
    elif 89 >= score >=75:
        return f"Оценка за {score} баллов: Хорошо."
    elif  74>= score >=50:
        return f"Оценка за {score} баллов: Удовлетворительно."
    elif score < 0 or score > 100:
        return "не может быть определена. Введите количество баллов в диапазоне от 0 до 100"
    else:
        return f"Оценка за {score} баллов: Неудовлетворительно."
score = int(input("Введите количество баллов: "))
result = check_grade(score)
print(f"Оценка за {score} баллов {result}")