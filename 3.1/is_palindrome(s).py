def is_palindrome(s):
    x=[]
    for b in s:
        if b.isalnum():
            x.append(b.lower())
    s="".join(s.split()).lower()
    reversed_s=x[::-1]
    return x == reversed_s
s=input("Введите строку")
print(is_palindrome(s))