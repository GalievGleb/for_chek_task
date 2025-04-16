def find_min(numbers):
    min=numbers[0]
    for n in numbers:
        if n < min:
            min=n
            print(f'Минимальное число из списка [{numbers}]:{min}')
numbers=input("Введите числа через пробел:").split()
find_min(numbers)
