def extract_subdict(my_dict, keys):
    new = {}
    for key in keys:
        if key in my_dict:
            new[key] = my_dict[key]
    return new

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))