def is_unique(s):
    seen = ""
    for word in s:
        if word in seen:
            return False
        seen += word
    return True



print(is_unique("hello"))