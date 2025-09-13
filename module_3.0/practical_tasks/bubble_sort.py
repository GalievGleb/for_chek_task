user_input = input("Введите числа через запятую: ")
numbers = [int(num.strip()) for num in user_input.split(',')]

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Обмен элементов
                flag = True
        if not flag:
            break
    return numbers

sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", ", ".join(map(str, sorted_numbers)))