year_of_birth = int(input('Введите год вашего рождения: '))
current_year = 2025

def age_message(y,c):
    age = c - y
    print(f"Ваш возраст: {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif age >= 18 and age <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

age_message(year_of_birth, current_year)