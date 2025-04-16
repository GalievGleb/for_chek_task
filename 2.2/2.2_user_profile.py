name = input(f"Привет! Как тебя зовут?")
job_q = input(f"{name}, как называется твоя профессия?")
fav_tool = input(f"{name}, какой твой любимый инструмент в тестировании? ")
if not fav_tool:
    print("Инструмент не указан")
else: print(f"{name}, ваш любимый инструмент: {fav_tool}, отличный выбор!")