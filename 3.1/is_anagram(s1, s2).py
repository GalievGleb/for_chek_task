def is_anagram(s1, s2):
    s1="".join(s1.split()).lower()
    s2="".join(s2.split()).lower()
    return sorted(s1)==sorted(s2)
s1=input("Введите первое слово:")
s2=input("Введите второе слово:")
print(is_anagram(s1, s2))
