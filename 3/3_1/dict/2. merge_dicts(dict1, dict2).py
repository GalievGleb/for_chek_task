def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))