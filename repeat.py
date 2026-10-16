def repeat(services):
    for service in services:
        name = service["name"]
        price = service["price"]
        duration = service["duration"]
        print(f"{name} - {price} руб. ({duration} мин.)")

services = [
    {"name": "массаж таяки", "price": 3000, "duration": 200},
    {"name": "массаж венки", "price": 2000, "duration": 100},
    {"name": "массаж пшо", "price": 1400, "duration": 60},
    {"name": "массаж нчт", "price": 2400, "duration": 80},
]

repeat(services)