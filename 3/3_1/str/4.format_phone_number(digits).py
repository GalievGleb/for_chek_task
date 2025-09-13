
def format_phone_number(digits):
    if digits.isdigit() and len(digits) == 10:
        first_digit = digits[0:3]
        second_digit = digits[3:6]
        third_digit = digits[6:10]
        return f"({first_digit}) {second_digit}-{third_digit}"
    else:   return "Неправильно набран номер"

print(format_phone_number("1234567890"))