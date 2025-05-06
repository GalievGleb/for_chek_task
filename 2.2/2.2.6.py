#  Задача 1: Добавление элемента в список
numbers = [1,2,3]
numbers.append(int(input("Введите число: ")))
print(numbers)

#  Задача 2: Удаление элемента из списка
fruits = ["Москва","Лондон","Париж"]
fruits.remove(input("Введите город для удаления: "))
print(fruits)

#  Задача 3: Доступ к элементу по индексу
fruits = ["Москва","Питер","Новосибирск", "Екатеринбург"]
len_list = len(fruits)
user_choose=int(input(f"Введите номер города от 1 до {len_list}:"))
print(fruits[user_choose-1])

#  Задача 4: Доступ к элементу по срезу списка
numbers = [0,1,2,3,4,5,6,7,8,9]
len_list = len(numbers)
user_choose=int(input(f"Введите первое число от 0 до {len_list-1}:"))
user_choose1=int(input(f"Введите второе число от {user_choose} до {len_list-1}:"))
print(numbers[user_choose:user_choose1])

#  Задача 5: Изменение элемента списка
colors = ["red","green","blue"]
len_list = len(colors)
user_choose=int(input(f"Введите номер цвета который хотите заменить от 1 до {len_list}:"))
colors[user_choose-1]=input(f"Введите цвет для замены:")
print(colors)

#  Задача 6: Узнаем длину списка
animals = ["cat","dog","rabbit", "hamster"]
len_list = len(animals)
print(len_list)

#  Задача 7: Добавление элемента в словарь
student = {"name":"Ivan","age":20}
student["grade"]=input(f"Введите ваш grade:")
print(student)

#  Задача 8: Изменение элемента словаря
student = {"name":"Ivan","age":20, "grade":"B"}
student["grade"]=input(f"Введите ваш grade:")
print(student)

#  Задача 9: Удаление элемента из словаря
student = {"name":"Ivan","age":20, "grade":"A"}
student_choose=input(f"Введите что из списка вы хотите увидеть:")
print(student[student_choose])

#  Задача 10: Доступ к элементу словаря по ключу
student = {"name":"Ivan","age":20, "grade":"A"}
student_choose=input(f"Введите что из списка вы хотите увидеть:")
student_choose =  student_choose.lower()
if student_choose == "name":
    print(f"Имя студента - {student['name']}")
if student_choose == "age":
    print(f"Возраст студента - {student['age']}")
if student_choose == "grade":
    print(f"Оценка студента - {student['grade']}")
else: print("poshel nahren")

#  Задача 11: Проверка наличия ключа в словаре
student = {"name":"Ivan","age":20, "grade":"A"}
student_choose=input(f"Введите что из списка вы хотите увидеть:")
student_choose =  student_choose.lower()
if student_choose in student:
    print(f"Ключ {student_choose} найден в словаре")
else: print(f"Ключ {student_choose} не найден в словаре")

#  Задача 12: Изменение элемента во вложенном словаре
student = {"name":"Ivan","address":{"city":"Moscow","street":"Lenina"}}
student_choose=input(f"Введите новый город:")
student["address"]["city"] = student_choose
print(student)

#  Задача 13: Изменение элемента в списке, находящемся в словаре
student = {"name":"Maria","grades":[75,82,90]}
choose_number = int(input("Выберите какую оценку изменить:"))
student_choose = int(input(f"Введите новую оценку:"))
student["grades"][choose_number] = student_choose
print(student)

#  Задача 14: Изменение элемента в словаре, находящемся внутри списка
student = [{"name":"Ivan","age":20}, {"name":"Petya","age":22}]
choose_student = input("Выберите чей возраст меняем:")
choose_student = choose_student.lower()
new_age = int(input(f"Введите новый возраст:"))
student['name' == choose_student]['age'] = new_age
print(student)

#  Задача 15: Проверка наличия элемента и определение длины кортежа
colors = ("red","green","blue")
user_choose=input(f"Введите цвет:")
len_list = len(colors)
if user_choose in colors:
    print(f"Наличие '{user_choose}': True. Длина кортежа: {len_list}")