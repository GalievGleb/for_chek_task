log_input = input("Введите строку лога: ").strip()
#текст для инпута 'Ошибка: тест не пройден из-за ошибки в модуле auth'
processed_log = log_input.replace("Ошибка", "Ошибка критическая", 1)
log_words = processed_log.split()
print("Обработанная строка:", processed_log)
print("Разбитый текст:", log_words)