#Задача 2: Поиск минимального числа в списке
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
print(find_min([3, 2, 4, 1, 5]))
