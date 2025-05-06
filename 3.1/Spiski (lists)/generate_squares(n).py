def generate_squares(n):
    numbers = [x ** 2 for x in range(1, n+1)]
    return numbers



print(generate_squares(5))  # [1, 4, 9, 16, 25]