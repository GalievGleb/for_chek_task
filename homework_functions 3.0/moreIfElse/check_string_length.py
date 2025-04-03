def check_string_length(string, length):
    if length<len(string):
         return "Строка слишком короткая"
    else:
        return "Длина строки достаточная"

string = input("Введите текст: ")
length = int(input("Введите число: "))
print(f"{check_string_length(string, length)}")