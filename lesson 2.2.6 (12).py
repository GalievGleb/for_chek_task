'''Изменение элемента во вложенном словаре'''

phyton_Copy_Edit_student={
    "name": "Ivan",
    "address": {
        "city": "Moscow",
        "street": "Lenina"
    }
}
phyton_Copy_Edit_student["address"]["city"]="Saint_Petersburg"
print(phyton_Copy_Edit_student)