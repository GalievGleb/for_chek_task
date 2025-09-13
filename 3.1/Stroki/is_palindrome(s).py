'''def is_palindrome(s):
    s1 = s.lower()[::-1].replace(" ","").replace(",","").replace(":","")
    s2 = s.lower().replace(" ","").replace(",","").replace(":","")
    if s1 == s2:
        return True
    else:
        return False'''

def is_palindrome(s):
    s1 = [s2.lower() for s2 in s if s2.isalnum()]
    return s1 == s1[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))