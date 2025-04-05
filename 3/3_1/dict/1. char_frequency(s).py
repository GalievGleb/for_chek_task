def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else: freq[char] = 1
    print(freq)

char_frequency("hello")