def repeatfind(services, name):
    for service in services:
        if service['name'].lower().strip() == name.lower().strip():
            return service
        None

services = [
    {"name": "модельная стрижка", "price": 500, "duration": 60},
    {"name": "бигуди", "price": 1000, "duration": 120},
    {"name": "выпрямление волос", "price": 2000, "duration": 200},
    {"name": "эрокез", "price": 4000, "duration": 300},
]

user_input = input("Какая услуга вас интересует? ").lower().strip()

result = repeatfind(services, user_input)

if result:
    print(f"Нашли: {result['name']}, {result['price']} руб. - ({result['duration']} мин.)")
else:
    print("Такой услуги нет")
