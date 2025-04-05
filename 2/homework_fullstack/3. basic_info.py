name=input("Добрый день, как вас зовут?:")
print(f"{name}! Добро пожаловать!")
profession=input("Какая ваша профессия?:")
age=input(f"Сколько лет вы работаете {profession}?:")
while True:
    answer = input("Отлично! Думаю, вы с легкостью ответите на вопрос. Что такое переменная?: ")

    if "хранилище" in answer or "контейнер" in answer or "значение" in answer or "ссылка" in answer:
        print("Верно!")
        break
    else:
        print("Неправильно, попробуйте еще раз.")
