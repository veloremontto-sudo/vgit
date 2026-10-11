age = int(input("Ваш возраст? "))
day = str(input("День недели? ").strip().lower())

if age <= 18 and day == "среда".strip().lower():
    discont = 0.60
elif age <= 18:
    discont = 0.50
elif day == "среда".strip().lower():
    discont = 0.10
else:
    discont = 0

final = 500 * (1 - discont)
print(f"Скидка: {discont * 100:.0f}%")
print(f"Итого: {final:.2f}")