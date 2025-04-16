def merge_dicts(dict1, dict2):
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    return dict1.update(dict2)

print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}