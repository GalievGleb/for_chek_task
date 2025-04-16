def group_by_first_letter(strings):
    a={}
    for s in strings:
        s1=s[0]
        if s1 not in a:
            a[s1]=[]
        a[s1].append(s)
    return a
a=input("Введите список").split()
print(group_by_first_letter(a))

