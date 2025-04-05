def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    chars1 = sorted(list(s1))
    chars2 = sorted(list(s2))
    if len(s1) != len(s2):
        return False
    elif chars1 == chars2:
        return True
    else: return False


print(is_anagram("listen", "silent"))


