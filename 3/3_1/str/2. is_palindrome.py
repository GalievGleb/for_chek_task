def is_palindrome(s):
    s = s.lower()
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c
    cleaned_reverse = cleaned[::-1]
    if cleaned == cleaned_reverse:
        return True
    else: return False


print(is_palindrome("A man, a plan, a canal: Panama"))
