def merge_lists(list1, list2):
    list1.extend(list2)
    result=[]
    for item in list1:
        if item not in result:
            result.append(item)
    print(result)

merge_lists([1, 2, 2, 3, 4, 4], [1, 2, 3, 4])
