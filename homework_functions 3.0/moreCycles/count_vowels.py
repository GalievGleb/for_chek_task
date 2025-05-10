def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in string.lower():
        if letter in vowels:
            count += 1

    return count

text = input("Введите текст: ")
print(f"Количество гласных в строке {text}: {count_vowels(text)}")