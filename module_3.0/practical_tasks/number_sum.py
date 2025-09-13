n = int(input('Введите число: '))

def number_sum(n):
    total_sum = 0
    print("Числа:", end=' ')
    for i in range(1, n + 1):
        print(i, end=' ')
        total_sum += i
    print()
    print("Сумма чисел:", total_sum)

number_sum(n)
