def calculator():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operator = input("Выберите операцию (+, -, *, /): ")

    def sum(a, b):
        return a + b
    def subtraction(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return 'Ошибка: деление на ноль'

    if operator == '+':
        result = sum(a, b)
    elif operator == '-':
        result = subtraction(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        result = 'Ошибка: неверная операция'

    print(f'Результат: {result}')

calculator()