import os
from gigachat import GigaChat


credentials = os.getenv("GIGACHAT_CREDENTIALS")


if not credentials:
    raise RuntimeError("Не задан GIGACHAT_CREDENTIALS")


with GigaChat(credentials=credentials) as client:
    response = client.chat.create("Привет! Ответь коротко, ты работаешь?")
    print(response.choices[0].message.content)