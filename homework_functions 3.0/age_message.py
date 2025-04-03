from datetime import datetime
def age_message():
    year_of_birth = int(input("Введите год вашего рождения: "))
    current_year = datetime.now().year
    age = current_year - year_of_birth
    print(f"Ваш возраст: {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif 18 <= age <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")
age_message()