def remove_duplicates(s):
    a=''
    for i in s:
        if i.lower() not in a.lower():
            a=a+i
    print(a)
s=input('Введите слово:')
remove_duplicates(s)

