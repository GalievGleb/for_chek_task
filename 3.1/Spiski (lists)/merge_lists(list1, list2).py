"""def merge_lists(list1, list2):
    result = []
    list3 = list1 + list2
    for num in list3:
        if num not in result:
            result.append(num)
    return result"""

def merge_lists(list1, list2):
    result = []
    seen = set()
    for num in list1 + list2:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result



print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
