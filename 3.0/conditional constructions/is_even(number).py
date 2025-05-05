"""def is_even(number):
    if number > 0 and number % 2 == 0:
       return "четным"
    else:
        return "нечетным"
number = 8
print(f"Число {number} является {is_even(number)}")"""

def is_even(number):
    return "четным" if number %2 == 0 else "нечетным"

number1 = 4
print(f"Число {number1} является {is_even(number1)}")
number2 = 9
print(f"Число {number2} является {is_even(number2)}")