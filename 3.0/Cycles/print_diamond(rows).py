#Задача 4: Ромбовидный треугольник
def print_diamond(rows):
    for i in range(1, rows + 1):
        print(' *' * i)

    for i in range(rows - 1, 0, -1):
        print(' *' * i)

print_diamond(4)


