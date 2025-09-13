def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    print(f"Минимальное число в списке {numbers}: {min_number}")

find_min([20, 9, 4, 7, 4])