def char_frequency(s):
    s=s.lower()
    a={}
    for i in s:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    return a
s=input('Введите слово:')
print(char_frequency(s))