#Задача 4: Группировка элементов по первому символу
'''Напишите функцию **`group_by_first_letter(strings)`**, которая принимает список строк и группирует их в словарь, где ключами являются первые символы строк, а значением — список строк, начинающихся с этого символа.

**Требования:**

- Функция должна принимать один аргумент: список строк **`strings`**.
- Верните словарь с группировкой.'''

def group_by_first_letter(strings):
    grouped = {}
    for string in strings:
        first_char = string[0]
        if first_char not in grouped:
            grouped[first_char] = [string]
        else:
            grouped[first_char].append(string)
    return  grouped


strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
    # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}