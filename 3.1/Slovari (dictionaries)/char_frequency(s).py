#Задача 1: Частотный анализ строки
'''Напишите функцию **`char_frequency(s)`**, которая создаёт словарь, где ключами являются символы строки, а значениями — количество раз, когда каждый символ встречается в строке.

**Требования:**

- Функция должна принимать один аргумент: строку **`s`**.
- Верните словарь с частотами символов.'''

def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

char_frequency("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}