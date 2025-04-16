def longest_word(s):
    s1 = s.replace(",","").split()
    return max(s1, key=lambda word: len(word))


print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))