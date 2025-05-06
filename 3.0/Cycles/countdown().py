#Задача 5: Обратный отсчёт и Задача 6: Обратный отсчёт - 2
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Старт")

countdown()

def countdown1():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Старт")

countdown1()