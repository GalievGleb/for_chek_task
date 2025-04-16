def born_to_die():
    birth_year = int(input("В каком году вы родились?"))
    current_year = 2025
    current_age = current_year - birth_year
    print("Ваш возраст:", current_age)
    if current_age < 18:
        print("Вы еще молоды, учеба - ваш путь!")
    if current_age >= 18 and current_age <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")
born_to_die()
