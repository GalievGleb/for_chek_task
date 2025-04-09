# текст лога для проверки программы " Ошибка: тест не пройден из-за ошибки в модуле auth"
def process_line():
    error_message = input('Введите строку лога: ')
    clean_text = error_message.strip()
    clean_text = clean_text.replace('Ошибка', 'Ошибка критическая')
    splited_text = clean_text.split()
    print(f'Обработанная строка: {clean_text}')
    print(f'Разбитый текст: {splited_text}')

process_line()