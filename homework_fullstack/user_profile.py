
name="Artem"
job="QA"
favorit_tool="Postman"

def change_favorit_tool(filed_tool, current_tool):
    while True:
        answer = input("Введите Ваш любимый инструмент для тестирования:")
        if not answer.strip():
            print("Инструмент не указан. Попробуйте снова!")
        else:
            return answer

favorit_tool = change_favorit_tool("Любимый инструмент для тестирования",favorit_tool)
print("\nОбновленные данные:")
print(f"Любимый инструмент для тестирования: {favorit_tool}")