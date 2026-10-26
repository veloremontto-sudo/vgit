histories = {
    111: [
        {"role": "Анна", "content": "Скрипят тормоза"}
    ],
    222: [
        {"role": "Максим", "content": "Проколол колесо"}
    ]
}

histories[222].append({
    "role": "Максим", "content": "Когда будет готово?"
})

histories[111].append({
    "role": "Анна", "content": "А сколько стоит ремонт?"
})

if 333 not in histories:
    histories[333] = []

histories[333].append({
    "role": "Игорь",
    "content": "Сколько стоит ремонт?"
})

print(f"История пользователей: {histories}")