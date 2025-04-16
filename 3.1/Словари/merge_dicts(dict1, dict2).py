def merge_dicts(dict1, dict2):
    a=dict1.copy()
    for key, value in dict2.items():
        if key in a:
            a[key]=a[key]+value
        else:
            a[key]=value
    return a