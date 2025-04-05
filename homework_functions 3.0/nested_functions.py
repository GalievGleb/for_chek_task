def calculator():
    # Вложенные функции для арифметических операций
    def plus(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def mnozh(x, y):
        return x * y

    def delit(x, y):
        if y == 0:
            return "Ошибка: деление на ноль!"
        return x / y

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == '+':
        result = plus(num1, num2)
    elif operation == '-':
        result = minus(num1, num2)
    elif operation == '*':
        result = mnozh(num1, num2)
    elif operation == '/':
        result = delit(num1, num2)
    else:
        result = "Ошибка: неверная операция!"

    print("Результат:", result)


calculator()