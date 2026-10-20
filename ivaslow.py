try:
    age = int(input("Возраст: "))
    print(f"Вам {age} лет")
except ValueError:
    print("Ошибка: нужно ввести число!")