import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise RuntimeError("Не задана переменная OPENAI_API_KEY")


client = OpenAI(api_key=api_key)


response = client.responses.create(
    model="gpt-4.1-mini",
    instructions="Ты - дружелюбный консультант кофейни. Отвечай кратко",
    input="Посоветуй напиток"
)


print(response.output_text)