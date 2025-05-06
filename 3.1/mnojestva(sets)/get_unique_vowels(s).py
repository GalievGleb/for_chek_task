#Задача 3: Получение уникальных гласных из строк
'''Создайте функцию **`get_unique_vowels(s)`**, которая принимает строку и возвращает
набор уникальных гласных, содержащихся в строке (игнорируя регистр).
**Требования:**
- Функция должна принимать один аргумент: строку **`s`**.
- Гласные буквы: **`a, e, i, o, u`**.
- Игнорируйте регистр символов.
- Верните множество уникальных гласных.'''

def get_unique_vowels(s):
    unique_vowels = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for element in s:
        if element in vowels:
            unique_vowels.add(element)
    return unique_vowels


print(get_unique_vowels("Hello World"))  # {'e', 'o'}