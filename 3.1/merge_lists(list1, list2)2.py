def merge_lists(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]
try:
    list1 = [int(x) for x in input("Введите первый список:").split()]
except ValueError:
    print("Введите только числа")
    exit()
try:
    list2 = [int(x) for x in input("Введите второй список:").split()]
except ValueError:
    print("Введите только числа")
    exit()
print(merge_lists(list1, list2))
