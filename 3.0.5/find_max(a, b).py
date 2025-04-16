def find_max(a, b):
    if a > b:
        print(f"Максимальное из чисел {a} и {b} : {a}" )
    elif a < b:
        print(f"Максимальное из чисел {a} и {b} : {b}" )
    else:
        print(f'Число {a} и {b} равны')
a=int(input("Введите первое число:"))
b=int(input("Введите первое число:"))
find_max(a, b)