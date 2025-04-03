def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Пример использования
numbers = input("Введите числа через запятую: ")
numbers = [int(num) for num in numbers.split(',')]
print(bubble_sort(numbers))

