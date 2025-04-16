def extract_subdict(my_dict, keys):
    a={}
    for key in keys:
        if key in my_dict:
            a[key]=my_dict[key]
    return a
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'c', 'd']
print(extract_subdict(my_dict, keys))