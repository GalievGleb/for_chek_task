# Задача 1: Удаление дубликатов
def remove_duplicates(lst: list):
    """f для проверки уникальности символов"""
    seen = set()
    final = []
    for char in lst:
        if char not in seen:
            seen.add(char)
            final.append(char)
    return final

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
print("--------------------------------------")

# Задача 2: Генерация списка квадратов
def generate_squares(n: int):
    """ f для генерации списка квадратов от 1 до n """
    power_list = []
    for i in range(1, n + 1):
        power_list.append(i**2)
    return power_list

print(generate_squares(5))  # [1, 4, 9, 16, 25]
print("--------------------------------------")

# Задача 3: Объединение двух списков
def merge_lists(list1: list, list2: list):
    """ f для объединение двух списков и удаления дубликатов """
    merged_list = list1 + list2
    without_duplicates = list(set(merged_list))
    return without_duplicates

print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
print("--------------------------------------")

# Задача 4: Проверка на отсортированность
def is_sorted(lst:list) -> bool:
    """ f для проверки отсортирован ли массив """
    sorted_list = sorted(lst)
    return lst == sorted_list

print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print("--------------------------------------")

# Задача 5: Слияние списков
def merge_lists(list1: list, list2: list):
    """ f для слияния списков двух списков одинаковой длины, выводящая новый список с результатами сложения  """
    i = 0
    sum_list = []
    for char in list1:
        sum_list.append(char + list2[i])
        i += 1
    return sum_list

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]

