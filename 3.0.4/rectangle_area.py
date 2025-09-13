def rectangle_area (a,b):
    area=a * b
    return area
a=int(input("Введите длину:"))
b=int(input("Введите ширину:"))
area=rectangle_area(a,b)
print( f'Площадь прямоугольника с длиной {a} и шириной {b} равна {area}')