def sum_numbers(n):
    total=0
    for i in range(1, n+1):
        total += i
    return total
n = int(input("Введите число: "))
print(f"Сумма чисел от 1 до {n}: {sum_numbers(n)}")