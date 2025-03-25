'''Проверка наличия элемента и определение длины кортежа'''

phyton_Copy_Edit_colors=("red", "green", "blue")
colors="green"
proverka=colors in phyton_Copy_Edit_colors
dlina=len(phyton_Copy_Edit_colors)
if colors in phyton_Copy_Edit_colors:
    print(f"Наличие '{colors}': {proverka}. Длина кортежа: {dlina}")
else:
    print(f"Наличие {colors}: {proverka}. Длина кортежа: {dlina}")