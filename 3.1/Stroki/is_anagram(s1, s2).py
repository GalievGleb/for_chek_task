def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))