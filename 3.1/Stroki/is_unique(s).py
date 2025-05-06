def is_unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False  
        seen.add(char)
    return True

print(is_unique("abcdef"))  # True
print(is_unique("hello"))  # False