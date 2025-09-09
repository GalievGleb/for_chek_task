def format_phone_number(digits):
     return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

print(format_phone_number("1234567890"))