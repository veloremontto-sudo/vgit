amount = float(input("Сумма покупки: "))

if amount > 5000:
    discount = 0.15
elif amount > 2000:
    discount = 0.10
elif amount > 1000:
    discount = 0.05
else:
    discount = 0

final = amount * (1 - discount)
print(f"Скидка: {discount * 100:.0f}%")
print(f"Итого: {final:.2f}")