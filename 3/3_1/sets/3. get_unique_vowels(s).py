def get_unique_elements(s):
    s = s.lower()
    vowels = set()
    for char in s:
        if char in "aeiou":
            vowels.add(char)
    return vowels

print(get_unique_elements("Hello World"))


