def check_string_length(string, length):
    if len(string) < length:
        return f"длинна {string} слишком короткая."
    else:
        return f"длинна строки {string} достаточна."
print(f"{check_string_length("Python", 5)}")
print(f"{check_string_length("Hi", 5)}")

