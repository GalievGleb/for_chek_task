# Задача 1: Анаграмма
def is_anagram(s1: str, s2: str)-> bool:
    """ f для проверки является ли строка анаграммой """
    str1 = sorted(s1.lower())
    str2 = sorted(s2.lower())
    return str1 == str2

print(is_anagram("listen", "silent")) # True
print(is_anagram("hello", "world")) # False
print("--------------------------------------")

# Задача 2: Палиндром
def is_palindrome(s: str) -> bool:
    """f для проверки, является ли строка палиндромом """
    str_letters = ''.join(filter(str.isalpha, s)).lower()
    reversed_str = str_letters[::-1]
    return str_letters == reversed_str

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))                        # True
print(is_palindrome("hello"))                           # False
print("--------------------------------------")

# Задача 3: Самое длинное слово
def longest_word(s: str):
    """f для выявления самого длинного слова в строке """
    words = s.split(' ')
    max_word = words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))  # "extraordinary”
print("--------------------------------------")

# Задача 4: Форматирование номера телефона
def format_phone_number(digits: str):
    """f для форматирования тел. номера / принимает строку из 10 цифр """
    part1 = digits[0:3]
    part2 = digits[3:6]
    part3 = digits[6:]
    result = "".join(["(", part1, ")", " ", part2, "-", part3])
    return result

print(format_phone_number("1234567890"))  # "(123) 456-7890”
print("--------------------------------------")

# Задача 5: Удаление дублирующихся символов
def remove_duplicates(s: str) -> str:
    """f для удаления дублирующихся символов """
    seen = set()
    final = []
    for char in s:
        if char not in seen:
            seen.add(char)
            final.append(char)
    return ''.join(final)

print(remove_duplicates("programming"))  # "progamin”
print(remove_duplicates("mmammaa.mm."))
print("--------------------------------------")

# Задача 6: Проверка на уникальность символов
def is_unique(s: str) -> bool:
    """f для проверки уникальности символов """
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
        else:
            return False
    return True

print(is_unique("abcdef"))  # True
print(is_unique("hello"))  # False