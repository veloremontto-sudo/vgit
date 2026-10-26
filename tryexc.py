while True:
    try:
        price = int(input("Введите стоимость ремонта: "))
        if price < 0:
            print("Ошибка: стоимость ремонта не может быть отрицательной.")
            continue
        
        print(f"Стоимость ремонта: {price} руб.")
        break
    except ValueError:
        print("Ошибка: введено не число. Пожалуйста, введите корректное значение.")
