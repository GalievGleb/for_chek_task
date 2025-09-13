def print_diamond(rows):
    for i in range(1, rows + 1):
        print("* " * i)

    for i in range(rows - 1, 0, -1):
        print("* " * i)

rom = int(input("Введите число: "))
print_diamond(rom)
