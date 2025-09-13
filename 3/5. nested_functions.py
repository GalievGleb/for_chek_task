def calculator():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /):")
    def dev(operation):
        if operation == "+":
            result = a + b
            print(result)
        elif operation == "-":
            result = a - b
            print(result)
        elif operation == "*":
            result = a * b
            print(result)
        elif operation == "/":
            result = a / b
            print(result)
        else: print("Введите корректную операцию")
    dev(operation)

calculator()