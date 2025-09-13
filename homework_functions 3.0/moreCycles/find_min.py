def find_min(numbers):
    min_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
numbers = list(map(float, input("Введите числа через пробел: ").split()))
print(f"Минимальное число в списке {numbers}: {find_min(numbers)}")