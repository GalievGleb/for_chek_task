def check_string_length(string, length):
    if len(string) > length:
        print(f"Длинна строки {string} достаточная")
    else:
        print(f"Длинна строки {string} слишком короткая")

check_string_length("Python", 5)
check_string_length("Hi", 5)