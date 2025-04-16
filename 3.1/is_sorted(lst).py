def is_sorted(lst):
    return lst==sorted(lst)
lst=input("Введите список")
lst=[int(a) for a in lst]
print(is_sorted(lst))