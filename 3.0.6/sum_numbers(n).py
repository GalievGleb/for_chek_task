def sum_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print(f'Сумма чисел от 1 до {n}:{sum}')
n=int(input("Введите целое число:"))
sum_numbers(n)