services = [
    {"name": "стрижка", "price": 600, "duration": 60},
    {"name": "маникюр", "price": 1000, "duration": 120},
    {"name": "укладка", "price": 300, "duration": 20},
    {"name": "педикюр", "price": 1100, "duration": 130},
    {"name": "массаж", "price": 3000, "duration": 230},
]

with open("services3.txt", "w", encoding="utf-8") as file:
    for service in services:
        file.write(f"{service['name']}; {service['price']}; {service['duration']}\n")