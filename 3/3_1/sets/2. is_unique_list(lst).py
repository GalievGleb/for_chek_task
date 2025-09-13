def is_unique_list(lst):
    if len(set(lst)) == len(lst):
        return True
    else: return False

print(is_unique_list([1, 2, 3, 4]))
print(is_unique_list([1, 2, 2, 3]))