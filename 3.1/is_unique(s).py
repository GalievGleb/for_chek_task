def is_unique(s):
    s1=s.replace(' ','')
    a=''
    for i in s1:
        if i not in a:
            a=a+i
    return a.lower()==s1.lower()
s=input('ВВЕДИТЕ СЛОВО:')
print(is_unique(s))