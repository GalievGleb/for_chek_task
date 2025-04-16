#Задача 3: Подсчёт гласных в строке
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i.lower() in vowels:
            count += 1
    return count
print(f"Количество гласных в строке: {count_vowels("Hello World")}")