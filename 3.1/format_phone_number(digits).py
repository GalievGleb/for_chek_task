def format_phone_number(digits):
    a=digits[:3]
    b=digits[3:6]
    c=digits[6:]
    if len(digits) ==10 and digits.isdigit():
        print(f'+7({a}) {b}-{c}')
    else:
        print("Неверный формат ")
digits=input("Введите номер без пробелов: +7")
format_phone_number(digits)