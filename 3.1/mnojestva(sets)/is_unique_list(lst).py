#Задача 2: Проверка списка на уникальность элементов
'''Напишите функцию **`is_unique_list(lst)`**, которая принимает список и возвращает **`True`**, если все элементы списка уникальны, и **`False`**, если есть повторения.

**Требования:**

- Функция должна принимать один аргумент: список **`lst`**.
- Верните **`True`**, если все элементы уникальны, иначе — **`False`**.'''

'''def is_unique_list(lst):
    unique_elements = []
    for element in lst:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements == lst'''

def is_unique_list(lst):
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False