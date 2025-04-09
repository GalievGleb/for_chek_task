# Задача 1: Частотный анализ строки
def char_frequency(s:str) -> dict:
    """ f для подсчета символов в строке """
    new_dict = {}
    for char in s:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict

print(char_frequency("hello"))    # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print("--------------------------------------")

# Задача 2: Слияние двух словарей
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """ f принимающая два словаря и объединяющая их в один. Если в обоих словарях
     есть одинаковые ключи, суммируйте их значения (значения только числа) """
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}
print("--------------------------------------")

# Задача 3: Обратное преобразование словаря в два списка
def dict_to_lists(my_dict: dict):
    """ f для преобразования словаря в два списка """
    keys = []
    values = []
    for key, value in my_dict.items():
        keys.append(key)
        values.append(value)
    return (keys, values)

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])

# Задача 4: Группировка элементов по первому символу
def group_by_first_letter(strings):
    """ f для группировка элементов по первому символу. Принимает список строк """
    grouped = {}
    for string in strings:
        first_letter = string[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(string)
    return grouped

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings)) # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
print("--------------------------------------")

# Задача 5: Извлечение подсловаря
def extract_subdict(my_dict: dict, keys):
    """ f для извлечения подсловаря """
    new_dict = {}
    for key, value in my_dict.items():
        if key in keys:
            new_dict[key] = value
    return  new_dict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}