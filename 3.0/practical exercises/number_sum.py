def numbers_sum():
    n = int(input("Введите число: "))
    numbers = list(range(1, n+1))
    print("Числа:", ' '.join(map(str, numbers)))
    total = sum(numbers)
    print("Сумма чисел:", total)
numbers_sum()
