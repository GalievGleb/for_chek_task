# Задача 1: Уникальные элементы списка
'''Напишите функцию **`get_unique_elements(lst)`**, которая принимает список чисел или строк и возвращает новый список, содержащий только уникальные элементы из исходного списка.

**Требования:**

- Функция должна принимать один аргумент: список **`lst`**.
- Верните список уникальных элементов.'''

def get_unique_elements(lst):
    unique_elements = []
    for element in lst:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]