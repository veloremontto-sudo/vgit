amount = int(input("Сумма рассхода: "))

with open("exspenses.txt", "a", encoding="utf-8") as file:
    file.write(f"{amount}" + "\n")