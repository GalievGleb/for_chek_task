def count_vowels(string):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for i in string.lower():
        if i in vowels:
            count += 1
    print(f'Количество гласных в тексте "{string}" : {count}')
string=input("ВВедите текст:")
count_vowels(string)