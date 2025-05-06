# Задача 2: Слияние двух словарей
'''Напишите функцию **`merge_dicts(dict1, dict2)`**, которая принимает два словаря и объединяет их в один. Если в обоих словарях есть одинаковые ключи, суммируйте их значения (значения только числа).

**Требования:**

- Функция должна принимать два аргумента: словари **`dict1`** и **`dict2`**.
- Если ключ присутствует в обоих словарях, сложите их значения.
- Верните объединённый словарь.'''

def merge_dicts(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        if key in merged:
            merged[key] += dict2[key]
        else:
            merged[key] = dict2[key]
    return merged
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}