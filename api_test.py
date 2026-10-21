import requests

try:
    url = "http://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)

    data = response.json()

    price = data["price"]

    print(f"Цена биткоина: {price}")

except requests.exceptions.ConnectionError:
    print("Ошибка: нет интернета или сервер недоступен!")