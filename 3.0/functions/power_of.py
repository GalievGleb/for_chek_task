def power_of(number, exponent=2):
    return number ** exponent

number = int(input("Число:"))
exponent_input = input("Степень: ")
exponent = int(exponent_input) if exponent_input else 2

print(f" Число {number} в степени {exponent} равно {power_of(number, exponent)}.")

