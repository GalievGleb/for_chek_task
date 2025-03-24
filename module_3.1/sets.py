# Уникальные элементы списка
def get_unique_elements(lst: list):
    """ f для поиска уникальных элементов словаря. Принимает список чисел или строк
     и возвращает новый список, содержащий только уникальные элементы из исходного списка. """
    my_set = set(lst)
    return my_set

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5] - это ответ по заданию/ тут, видимо опечатка
print("--------------------------------------")

# Задача 2: Проверка списка на уникальность элементов
def is_unique_list(lst: list)-> bool:
    """ f для проверки списка на уникальность """
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False
print("--------------------------------------")

# Задача 3: Получение уникальных гласных из строки
def get_unique_vowels(s: str):
    """ f для получения уникальных гласных в строке """
    vowels = "aeiou"
    lower_str = s.lower()
    chars_list = [char for char in lower_str if char in vowels]
    unique_vowels = list(set(chars_list))
    return unique_vowels

print(get_unique_vowels("Hello World"))  # {'e', 'o'}