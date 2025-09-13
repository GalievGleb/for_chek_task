def remove_duplicates(lst):
    duplicates = []
    for item in lst:
        if item not in duplicates:
            duplicates.append(item)
    print(duplicates)

remove_duplicates([1, 2, 2, 3, 4, 4])