def calculator():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Выбери операцию: +, -, *, /")

    def plus(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Ошибка деления на 0"
        return a / b

    if operation == "+":
        result = plus(a,b)
    elif operation == "-":
        result = minus(a, b)
    elif operation == "*":
        result = multiplication(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Неверная операция"

    print(f"Результат: {result}")

calculator()