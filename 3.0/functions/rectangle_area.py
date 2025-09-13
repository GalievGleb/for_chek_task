"""a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def rectangle_area(a, b):
    return a * b
print(f"Площадь прямоугольника с длиной {a} и шириной {b} равна {rectangle_area(a, b)}")"""

def rectangle_area(length, width):
    return length * width

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"Площадь прямоугольника с длиной {a} и шириной {b} равна {rectangle_area(a,b)}")