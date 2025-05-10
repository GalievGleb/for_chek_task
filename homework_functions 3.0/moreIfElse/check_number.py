def check_number(number):
    if number>=0:
        if number % 2 == 0:
            return "положительное и четное"
        elif number % 2 != 0:
            return "положительное и нечетное"
    else:
        return "отрицательное"

number = int(input("Введите число: "))
print(f"Число {number} {check_number(number)}")