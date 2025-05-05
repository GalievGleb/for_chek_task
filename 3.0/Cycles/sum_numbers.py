#Задача 1: Сумма чисел от 1 до N
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = 5
print(sum_numbers(n))