import random

secret_random = random.randint(1, 100)

while True:
    try:
        user_number = int(input("Угадай число от 1 до 100! "))

        if user_number < secret_random:
            print("Загаданное число больше")
        elif (user_number > secret_random):
            print("Загаданное число меньше")
        else:
            print("Победа!!!")
            break
    except ValueError:
        print("Ошибка: Введите целое число!")