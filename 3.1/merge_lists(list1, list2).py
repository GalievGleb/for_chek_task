def merge_lists(list1, list2):
    s=set()
    result=[]
    for item in list1+list2:
        if item not in s:
            s.add(item)
            result.append(item)
    return result
list1=[x for x in input("Введите первый список:").split() if x]
list2=[x for x in input("Введите второй список:").split() if x]
print(merge_lists(list1,list2))