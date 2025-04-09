#задача 1: определяем кол-во полных кг
def grams_to_kilograms(grams):
    kilograms = grams // 1000
    return kilograms

grams = 12345
kilograms = grams_to_kilograms(grams)
print(f"Задача 1: В {grams} граммах содержится {kilograms} полных килограмм.")

#задача 2: вывод последней цифры числа
def print_last_digit(number):
    last_digit = number % 10
    return last_digit

number = 1234
last_digit = print_last_digit(number)
print(f"Задача 2: Последняя цифра числа {number}: {last_digit}")

#задача 3: определение, является ли число четным и положительным
print("Задача 3:")
def positive_and_even(number):
    if number > 0 and number % 2 == 0:
        print(f"Число {number} положительное и четное.")
    else:
        print(f"Число {number} не подходит под условия.")

number_1 = 14
number_2 = -4
number_3 = 15

result_1 = positive_and_even(number_1)
result_2 = positive_and_even(number_2)
result_3 = positive_and_even(number_3)

#задача 4: определение, выходит ли число за допустимый диапазон
print("Задача 4:")
def is_in_the_range(number):
    if number >= 0 and number <= 100:
        print(f"Число {number} находится в пределах диапазона от 0 до 100.")
    else:
        print(f"Число {number} выходит за пределы диапазона от 0 до 100.")

num_1 = 150
num_2 = 50

result_1 = is_in_the_range(num_1)
result_2 = is_in_the_range(num_2)

#задача 5: проверка, что число не кратно 3
print("Задача 5:")
def multiple_of_three(number):
    if number % 3 != 0:
        print(f"Число {number} не кратно 3.")
    else:
        print(f"Число {number} кратно 3.")

number_1 = 10
number_2 = 9

result_1 = multiple_of_three(number_1)
result_2 = multiple_of_three(number_2)