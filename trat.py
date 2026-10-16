total = 0

with open("exspenses.txt", "r", encoding="utf-8") as file:
    for line in file:
        amount = float(line.strip())
        total += amount

print(f"Всего расходов: {total}")