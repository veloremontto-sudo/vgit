query = input("Какая услуга вас интересует? ").strip().lower()

services = [
    {"name": "стрижка", "price": 600, "duration": 60},
    {"name": "маникюр", "price": 1000, "duration": 120},
    {"name": "укладка", "price": 300, "duration": 20},
    {"name": "педикюр", "price": 1100, "duration": 130},
    {"name": "массаж", "price": 3000, "duration": 230},
]

found = False

for service in services:
    if service["name"].lower() == query.lower():
        print(f"{service['name']} - {service['price']} руб. ({service['duration']} мин.)")
        found = True
    elif service["price"] > 1000:
        print(f"{service['name']} - {service['price']} руб. ({service['duration']} мин.)")
        found = True

if not found:
    print("Такой услуги нету")
