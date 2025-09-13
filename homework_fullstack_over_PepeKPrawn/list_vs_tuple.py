import random
random_numbers = [random.randint(1, 10) for _ in range(5)]
random_tuple = tuple(random_numbers)
print(f"Исходный список: {random_numbers}")
print(f"Исходный кортеж: {random_tuple}")

random_numbers[1] = random.randint(1, 10)
print(f"\nИзмененный список: {random_numbers}")
try:
    random_tuple[1] = random.randint(1, 10)
except TypeError:
    print(f"Ошибка: Кортеж нельзя изменить!")

random_numbers.append(random.randint(1, 10))
print(f"\nДобавленный элемент в список: {random_numbers}")
try:
    random_tuple [1] += (random.randint(1, 10),)
except TypeError:
    print(f"Ошибка: В кортеж нельзя добавить элемент!")
