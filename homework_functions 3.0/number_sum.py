def number_sum():
    n = int(input("Введите число: "))
    print("Числа:", end=" ")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

    sum_numbers = 0
    counter = 1
    while counter <= n:
        sum_numbers += counter
        counter += 1

    print(f"Сумма чисел: {sum_numbers}")

number_sum()
