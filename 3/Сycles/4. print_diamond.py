def print_diamond(n):
    w = "*"
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))



print_diamond(4)