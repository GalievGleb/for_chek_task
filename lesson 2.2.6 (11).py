'''Проверка наличия ключа в словаре'''

student={
    "name": "Ivan",
    "age": 20,
    "grade": "A"
}
if "grade" in student:
    print(f"Ключ '{"grade"}' найден в словаре")
else:
    print(f"Ключ '{"grade"}' не найден в словаре")

'''Если ключа нет в словаре'''

student={
    "name": "Ivan",
    "age": 20,
}
if "grade" in student:
    print(f"Ключ '{"grade"}' найден в словаре")
else:
    print(f"Ключ '{"grade"}' не найден в словаре")