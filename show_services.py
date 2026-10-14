

def show_services(services):
    for service in services:
        name = service["name"]
        price = service["price"]
        duration = service["duration"]
        print(f"{name} - {price} руб. ({duration} мин.)")

services = [
    {"name": "Стрижка", "price": 600, "duration": 60},
    {"name": "Маникюр", "price": 1000, "duration": 120},
]

show_services(services)