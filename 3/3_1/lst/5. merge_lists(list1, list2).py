def merge_lists(list1, list2):
    new_list = [list1[i] + list2[i] for i in range(len(list1))]
    return new_list

print(merge_lists([1, 2, 3], [4, 5, 6]))