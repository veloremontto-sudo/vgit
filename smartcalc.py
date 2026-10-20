try:
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    op = input("Операция (+,-,*,/): ")
# запрос к пользователю для задания переменных

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    # операции над переменными

except ValueError:
    print("Ошибка: введите число!")
except ZeroDivisionError:
    print("Ошибка: на 0 делить нельзя")