services = []

with open("repeat_services.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(";")
        services.append({
            "name": parts[0],
            "price": int(parts[1]),
            "duration": int(parts[2])
        })

print(services)