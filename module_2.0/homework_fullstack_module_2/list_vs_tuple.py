new_list = [4, 7, 9, 2, 5]
new_tuple = (4, 7, 9, 2, 5)

try:
    new_list[1] = 101
    print(f'Измененный список: {new_list}')
    new_tuple[1] = 101
    print(f'Измененный кортеж: {new_tuple}')
except Exception as e:
    print(f'Ошибка: Кортеж нельзя изменить!')
try:
    new_list.append(101)
    print(f'Добавленный элемент в список: {new_list}')
    new_tuple.append(101)
    print(f'Измененный кортеж: {new_tuple}')
except Exception as e:
    print(f'Ошибка: В кортеж нельзя добавить элемент!.')
