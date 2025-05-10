def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    n = 0
    for char in string:
        if char.lower() in vowels:
            n += 1
    print (f"Количество гласных в строке {string}: {n}")

count_vowels("Hello World")