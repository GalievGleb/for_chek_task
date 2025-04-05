name=input("Добрый день, как вас зовут?:")
print(f"{name}! Добро пожаловать!")
profession=input("Какая ваша профессия?:")
while True:
    tool=input(f"Введите ваш любимый инструмент в {profession}?:")

    if not tool:
        print("Инструмент не указан, попробуйте еще раз")
    else:
        print(f"Ваш любимый интремен: {tool}. Отличный выбор!")
        break
