
def find_service(services, name):
    for service in services:
        if service["name"].lower().strip() == name.lower().strip():
            return service
    return None


# --- База услуг ---
services = [
    {"name": "Стрижка", "price": 600, "duration": 60},
    {"name": "Маникюр", "price": 1000, "duration": 120},
    {"name": "Укладка", "price": 300, "duration": 20},
    {"name": "Педикюр", "price": 1100, "duration": 130},
    {"name": "Массаж", "price": 3000, "duration": 230},
]


# --- Программа спрашивает пользователя ---
user_input = input("Какая услуга вас интересует? ")

# --- Ищем ---
result = find_service(services, user_input)

# --- Показываем результат ---
if result:
    print(f"Нашли: {result['name']} - {result['price']} руб. ({result['duration']} мин.)")
else:
    print("Такой услуги нет")