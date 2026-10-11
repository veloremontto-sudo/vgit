age = int(input("Возраст: "))
has_ticket = input("Есть билет? (да/нет): ")

if age >= 18 and has_ticket == "да":
    print("Проходите")
else:
    print("Проход запрещен")