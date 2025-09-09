def check_number(number):
    if number % 2 == 0:
            if number > 0:
                return "четным и положительное"
            elif number < 0:
                return "четным и отрицательным"
    elif number % 2 != 0 and number < 0:
        return "нечетным и отрицательным"
    else:
        return "нечетным и положительным"

number1 = -4
print(f"Число {number1} является {check_number(number1)}")
number2 = 9
print(f"Число {number2} является {check_number(number2)}")