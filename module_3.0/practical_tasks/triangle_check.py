a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))
def triangle_check(a, b, c):
    if a <= (b + c) and b <= (a + c) and c <= (a + b):
        if a == b == c:
            print("Результат: Треугольник равносторонний.")
        elif a == b or a == c or c == b:
            print("Результат: Треугольник равнобедренный.")
        else:
            print("Результат: Треугольник разносторонний.")
    else:
        print("Треугоник с такими сторона не сущесвует")

triangle_check(a, b, c)