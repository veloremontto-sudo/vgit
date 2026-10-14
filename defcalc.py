number1 = int(input("Какое первое число?"))
number2 = int(input("Какое второе число?"))

def add(a, b):
    return a + b, a * b, a - b, a / b 

result = add(number1, number2)
print(result)