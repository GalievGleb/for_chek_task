name = input("Введите Ваше имя:")
job = input("Введите Вашу профессию:")
print(f"Привет {name} {job}! Добро пожаловать в мир Phyton для тестировщиков.")

answer = "Это ярлыки"
while True:
    question = input("Что такое переменная?")
    if question == answer:
        print("Ответ верный!")
        break
    else:
        print("Ответ неверный, подумай еще!)")

