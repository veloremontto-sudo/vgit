import asyncio
import os

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Не задана переменная BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💈 Услуги"),
            KeyboardButton(text="💰 Цены"),
        ],
        [
            KeyboardButton(text="📞 Контакты"),
            KeyboardButton(text="📍 Адрес"),
        ],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Выберите пункт меню 👇",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "💈 Услуги")
async def services_handler(message: Message):
    await message.answer("Наши услуги:\n✂️ Мужская стрижка\n🧔 Стрижка бороды\n💈 Комплекс")

@dp.message(F.text == "💰 Цены")
async def prices_handler(message: Message):
    await message.answer("Наш прайс:\n" "Мужская стрижка - 500 руб.\n" "Стрижка бороды - 250 руб.\n" "Комплекс - 700 руб.")


@dp.message(F.text == "📞 Контакты")
async def contact_handler(message: Message):
    await message.answer(
        "Связаться с нами: @barbershop_admin"
    )

@dp.message(F.text == "📍 Адрес")
async def address_handler(message: Message):
    await message.answer(
        "Мы находимся по адресу: Hauptstrabe 10"
    )

    
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - запустить бота\n"
        "/help - помощь\n"
        "/price - посмотреть цены\n"
        "/contact - связаться с нами"
    )

@dp.message(Command("contact"))
async def contact_handler(message: Message):
    await message.answer(
        "Связаться с нами: @barbershop_admin"
    )


@dp.message(Command("price"))
async def price_handler(message: Message):
    await message.answer(
        "Наш прайс:\n"
        "Мужская стрижка - 500 руб.\n"
        "Стрижка бороды - 250 руб.\n"
        "Комплекс - 700 руб."
    )


def get_ai_answer(user_text):
    return f"Тестовый ИИ получил сообщение: {user_text}"

@dp.message()
async def chat_with_ai(message: Message):
    answer = get_ai_answer(message.text or "")
    await message.answer(answer)

@dp.message()
async def echo_handler(message: Message):
    await message.answer("Ты написал: " + message.text)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())