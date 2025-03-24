#задача 1: добавление элемента в список
def add_el_to_end(arr, num):
    arr.append(num)
    print(arr)

numbers = [1,2,3]
num = 4
result = add_el_to_end(numbers, num)

#задача 2: удаление элемента из списка
def delete_element(arr, element):
    arr.remove(element)
    print(f"{element}: {arr}")

cities = ["Москва", "Париж", "Лондон"]
element = "Лондон"
new_cities_list = delete_element(cities,element)

#задача 3: доступ к элементу по индексу
def get_by_index(arr, index):
    element = arr[index]
    print(f"{element} - это город под индексом {index}")

cities = ["Москва", "Питер", "Новосибирск", "Екатеринбург"]
index = 2

city = get_by_index(cities, index)

#задача 4: доступ к элементу по срезу списка
def slice_subarray(arr, start, end):
    subarray = arr[start:end]
    print(f"Полученный срез: {subarray}")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start = 3
end = 7

result = slice_subarray(numbers, start, end)

#задача 5: изменение элемента списка
def change_color(arr, index, color):
    arr[index] = color
    print(arr)


colors = ["red", "green", "blue"]
color = "yellow"
index = 1

new_color_list = change_color(colors, index, color)

#задача 6: узнаем длину списка
def which_length(arr):
    length = len(arr)
    print(length)

animals = ["cat", "dog", "rabbit", "hamster"]
arr_length = which_length(animals)

#задача 7: добавляем элемент в словарь
def add_pair_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

student = {"name": "Ivan", "age": 20}
key = "grade"
value = "A"

print(add_pair_to_dictionary(student,key,value))

#задача 8: изменение элемента словаря
def change_value_in_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

student = {"name": "Ivan", "age": 20, "grade": "A"}
key = "grade"
value = "B"

print(change_value_in_dictionary(student,key,value))

#задача 9: удаление элемента словаря
def delete_pair(dictionary, key):
    del dictionary[key]
    return dictionary

student = {"name": "Ivan", "age": 20, "grade": "A"}
key = "age"

print(delete_pair(student,key))

#задача 10: доступ к элементу словаря по ключу
def get_name(dictionary):
    name = dictionary.get("name")
    print(f"Имя студента: {name}.")

student = {"name": "Ivan", "age": 20, "grade": "A"}
result = get_name((student))

#задача 11: проверка наличия ключа в словаре
def check_key(dictionary, key):
    if key in dictionary:
        print(f"Ключ {key} найден в словаре.")
    else:
        print(f"Ключ {key} не найден в словаре.")

student = {"name": "Ivan", "age": 20, "grade": "A"}
result = check_key(student, "grade")

#задача 12: изменение элемента во вложенном словаре
def change_city(dictionary, new_city):
    dictionary["address"]["city"] = new_city
    print(dictionary)

student = {"name": "Ivan", "address": {"city": "Moscow", "street": "Lenina"}}
new_city = "Saint Petersburg"
result = change_city(student, new_city)

#задача 13: изменение элемента в списке, находящемся в в словаре
def change_grade(dictionary, new_grade):
    dictionary["grades"][0] = new_grade
    print(dictionary)

student = {"name": "Maria", "grades": [75, 82, 90]}
new_grade = 85
result = change_grade(student, new_grade)

#задача 14: изменение элемента в словаре, находящемся внутри списка
def update_age(students, name, new_age):
    for student in students:
        if student["name"] == name:
            student["age"] = new_age
            break
    return students

students = [{"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22}]

updated_students = update_age(students, "Petya", 23)
print(updated_students)

#задача 15: проверка наличия элемента и определения длины кортежа
def check_element_and_lenght(tuple, element):
    is_element_in_tuple = element in tuple
    tuple_length = len(tuple)

    return is_element_in_tuple, tuple_length

colors = ("red", "green", "blue")
result = check_element_and_lenght(colors, "green")
print(f"Наличие 'green': {result[0]}. Длина кортежа: {result[1]}")

#----------------------------------
'''Задача 10: Доступ к элементу словаря по ключу'''

student2 = {
    'name': 'Ivan',
    'age': 20,
    'grade': 'A'
}
print(f'Имя студента: {student2['name']}')
print(f"Имя студента: {student2['name']}") #правильное использование кавычек

print(f'Имя студента: {student2['city']}')
print(f"Имя студента: {student2['city']}")  #правильное использование кавычек