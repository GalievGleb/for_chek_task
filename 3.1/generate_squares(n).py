def generate_squares(n):
    return [x**2 for x in range(1,n+1)]
while True:
    try:
        n=int(input('Введите целое число:'))
        print(generate_squares(n))
        break
    except ValueError:
        print('Ошибка!Введите целое число:')