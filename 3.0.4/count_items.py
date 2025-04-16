def count_items(*args):
    arg=input("Введите аргументы через пробел:")
    a=arg.split()
    dlina=len(a)
    print(f'Количество переданных элементов: {dlina}')
count_items()