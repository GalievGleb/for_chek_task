def check_string_length(string, length):
    if len(string) >= length:
        print(f'Длина "{string}" достаточная')
    else:
        print(f'Строка "{string}" слишком короткая')
string=input("Введите строку:")
length= int(input("Введите длину:"))
check_string_length(string, length)