def convert_seconds (seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    return hour, minute

sec=9765

result = convert_seconds(sec)

print(f"В {sec} секундах содержится {result[0]} час(ов) и {result[1]} минут(ы)")