
def convert_seconds(seconds):
    hours = seconds // 3600
    mins = hours // 60
    return (hours, mins)

seconds = int(input("введите количество секунд: "))
hours, mins = convert_seconds(seconds)
print(f" В {seconds} секундах содержится {hours} часов и {mins} минут")