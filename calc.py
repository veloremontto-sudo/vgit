bill = float(input("Сумма счета: "))
tip_percent = float(input("Процент чаевых: "))

tip = bill * tip_percent / 100
total = bill + tip

print(f"Чаевые: {tip:.2f}")
print(f"Итого: {total:.2f}")