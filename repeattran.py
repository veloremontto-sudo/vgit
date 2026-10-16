services = [
    {"name": "модельная стрижка", "price": 500, "duration": 60},
    {"name": "бигуди", "price": 1000, "duration": 120},
    {"name": "выпрямление волос", "price": 2000, "duration": 200},
    {"name": "эрокез", "price": 4000, "duration": 300},
]

with open("repeat_services.txt", "w", encoding="utf-8") as file:
    for service in services:
        file.write(f"{service['name']}; {service['price']}; {service['duration']}" + "\n")