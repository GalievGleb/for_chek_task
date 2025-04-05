def remove_duplicates(s):
    seen = ""
    for word in s:
        if word not in seen:
            seen += word
    return seen

print(remove_duplicates("programming"))