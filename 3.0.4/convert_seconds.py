def convert_seconds(sec):
    hour= sec//3600
    ostatok_hour=sec%3600
    minut=ostatok_hour//60
    second=ostatok_hour%60
    print(f'В {sec} секундах содержится {hour} час(ов) и {minut} минут(ы) и {second} секунд(ы)')
    return hour, minut, second
while True:
    try:
        sec = int(input("Введите количество секунд: "))
        break
    except ValueError:
        print("Неверный формат секунд, введите целое число:")
convert_seconds(sec)
##сделал с секундами , так как так больше нравится , а чтоб сделать как по заданию , нужно просто сделать округление в большую сторону при расчете минут.