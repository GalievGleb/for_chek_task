def group_by_first_letter(strings):
    groups = {}
    for word in strings:
        first_letter = word[0]
        if first_letter in groups:
            groups[first_letter].append(word)
        else:
            groups[first_letter] = [word]
    return groups

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))