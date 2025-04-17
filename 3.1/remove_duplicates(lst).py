def remove_duplicates(lst):
    lst1 = lst.replace(' ', '')
    a=[]
    for i in lst1:
        if i not in a:
            a.append(i)
    print(a)
lst=input("Введите список:")
remove_duplicates(lst)
