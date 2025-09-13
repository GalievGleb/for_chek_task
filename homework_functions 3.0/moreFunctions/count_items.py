def count_items(*args):
    return len(args)

items_count = count_items(1, 2, 3, 4, 5)
print(f"Количество переданных элементов: {items_count}.")

items_count = count_items("apple", "banana", "cherry")
print(f"Количество переданных элементов: {items_count}.")
