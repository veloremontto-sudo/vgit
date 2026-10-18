master1 = {
    "name1": "Иван",
    "experience": 4,
    "specialization": "Парикмахер",
    "available_times": [ "10:00", "14:00", "16:00", "18:00", "20:00" ]
}
service = [
    {"name": "стрижка"},
    {"price": 600},
    {"master": master1}
]

print(f"Мастер {service[2]['master']['name1']} (опыт {service[2]['master']['experience']} года) делает {service[0]['name']}")

for time in master1["available_times"]:
    print(f"{master1['name1']} свободен в {time}")




appointments = [ 
    { "client": "Анна", "service": "Стрижка", "time": "14:00" },
    { "client": "Жанна", "service": "Стрижка", "time": "16:00"}
]

print(f"{appointments[0]['client']} записана на {appointments[0]['service']} в {appointments[0]['time']}")




print(f"Свободное время у мастера {master1['name1']}:")

for time in master1["available_times"]:
    
    is_busy = False

    for appointment in appointments:
        if appointment["time"] == time:
            is_busy = True
            break
    if not is_busy:
        print(f"- {time}")