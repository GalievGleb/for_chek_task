def check_number(number):
    if number>0:
        if number%2==0:
            print(f'Число {number} положительное и четное')
        else:
            print(f'Число {number} положительное и нечетное')
    else:
        print(f'Число {number} отрицательное')
number=int(input('введите целое число:'))
check_number(number)

