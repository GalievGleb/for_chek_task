def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c

f = 100
c = fahrenheit_to_celsius(f)

print(f"{f} градусов по Фаренгейту это {c:.2f} Цельсия.")