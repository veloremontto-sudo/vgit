import requests

url = "http://httpbin.org/post"

application = {
    "name": "Анна",
    "service": "Стрижка",
    "time": "14:00",
    "master": "Иван"
}

try:

    response = requests.post(url, json=application)

    result = response.json()

    print("Заявка успешно отправлена!")
    print("Сервер получил:", result["json"])

except requests.exceptions.ConnectionError:
    print("Ошибка: сервер недоступен")