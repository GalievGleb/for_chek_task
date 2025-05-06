def merge_lists(list1, list2):
    return [x + y for x,y in zip(list2,list1)]

print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]