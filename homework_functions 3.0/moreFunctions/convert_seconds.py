def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return (hours, minutes)

total_seconds = int(input("Введите количество секунд: "))
hours, minutes = convert_seconds(total_seconds)
print(f"В {total_seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).")


