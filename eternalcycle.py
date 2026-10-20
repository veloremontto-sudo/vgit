while True:
    try:
        age = int(input("Введите число: "))

        if 1 <= age <= 100:
            print("Спасибо! ")
            break
        else:
            print("Ошибка: возраст должен быть от 1 до 100. Попробуйте еще раз.")
    except ValueError:
        print("Ошибка: нужно ввести число. Попробуйте еще раз.")