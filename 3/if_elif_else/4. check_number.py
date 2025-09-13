def check_number(number):
    if number > 0 and number % 2 == 0:
        print(f"Число {number} положительное и чётное")
    elif number < 0:
        print(f"Число {number} отрицательное")

check_number(-9)
check_number(20)