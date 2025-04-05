def age_message(year):
    age = 2025 - year
    print(f"Ваш возраст {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif  18 <= age <= 65:
        print("Отличный возраст для карьерного роста!")
    elif age > 100:
        print("Пора наслаждаться заслуженным отдыхом!")


user_year = int(input("Введите год вашего рождения: "))

age_message(user_year)