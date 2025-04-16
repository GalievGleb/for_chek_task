def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

char_frequency("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}