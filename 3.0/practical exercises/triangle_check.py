'''def check_triangle():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    if a < b + c and b < a + c and c < a + b:
        if a == b and b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник не получится")
check_triangle()'''


def check_triangle(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b):
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or a == c or b == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник не получится"

def main():
    try:
        a = int(input("Введите длину первой стороны: "))
        b = int(input("Введите длину второй стороны: "))
        c = int(input("Введите длину третьей стороны: "))

        result = check_triangle(a, b, c)
        print(f"Результат: {result}.")
    except ValueError:
        print("Ошибка: введены некорректные данные")
main()