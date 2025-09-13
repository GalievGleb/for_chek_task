purchase_amount = float(input("Введите сумму покупки: "))
discount_percent = float(input("Введите процент скидки: "))
discount_amount = (purchase_amount * discount_percent) / 100
final_amount = purchase_amount - discount_amount
rounded_final_amount = round(final_amount)
print(f"\nВы экономите: {discount_amount}")
print(f"Сумма к оплате (округлено): {rounded_final_amount}")
