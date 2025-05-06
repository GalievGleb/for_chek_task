#Задача 3: Максимальное из двух чисел
def find_max(a, b):
    return a if a > b else b
a = 10
b = 20
print(f"Максимальное из {a} и {b}: {find_max(a,b)}.")