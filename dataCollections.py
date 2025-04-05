#задача 1
animals = ["cats", "dogs", "hamsters"]
animals.append("birds")
print(animals)

#задача 2
snacks = ["chips", "nuts", "popcorn"]
snacks.remove("nuts")
print(snacks)

#задача 3
smartPhones = ["iphone", "xiaomi", "huawei"]
print(smartPhones[2])

#задача 4
jewelry = ["кольцо", "серьги", "браслет", "кафф", "лабрет", "подвеска", "цепочка", "колье"]
print(jewelry[3:7])

#задача 5
hair = ["short", "long", "straight"]
hair[2]="curly"
print(hair)

#задача 6
colors = ["blue", "white", "red", "yellow", ["rainbow","multicolor"]]
lenList=len(colors)
print(lenList)

#задача 7
superHero = {
    "name": "Tony",
    "lastName": "Stark"
}
superHero["nick"]= "IronMan"
print(superHero)

#задача 8
superHero = {
    "name": "Tony",
    "lastName": "Stark",
    "nick": "IronMan"
}
superHero["nick"]= "IronMan1"
print(superHero)

#задача 9
superHero = {
    "name": "Tony",
    "lastName": "Stark",
    "nick": "IronMan"
}
del superHero["nick"]
print(superHero)

#задача 10
superHero = {
    "name": "Tony",
    "lastName": "Stark",
    "nick": "IronMan"
}
print("Имя студента "+superHero["name"])

#задача 11
superHero = {
    "name": "Tony",
    "lastName": "Stark",
    "nick": "IronMan"
}
key = "name"
if key in superHero:
    print("Ключ "+key+" найден в словаре")
else:
    print("Ключ "+key+" не найден в словаре")

#задача 12
superHero = {
    "name": "Tony",
    "lastName": "Stark",
    "nick": "IronMan",
    "workPlace":{
        "name": "Башня Мстителей",
        "address":"Пятая авеню, Манхэттен, Нью-Йорк."
    }
}
superHero["workPlace"]["address"] = "890 Пятая авеню, Манхэттен, Нью-Йорк."
print(superHero)

#задача 13
student = {"name": "Анатолий",
           "lastName":"Полено",
           "marks":[3,4,3,5]
}
student["marks"][0]=5
print(student)

#задача 14
list1 = [1,2,3,{"fruit":"waterMelon","смысл жизни":42}]
list1[3]["fruit"]="apple"
print(list1)

#задача 15
elements=("fire","water","ground")
key="fire"
if key in elements:
    print("Наличие '"+key+"'. Длина кортежа " + str(len(elements)))
else:
    print("Отсутствие '"+key+"'. Длина кортежа " + str(len(elements)))