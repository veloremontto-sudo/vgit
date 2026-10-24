
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Не задана переменная BOT_TOKEN")


class Booking(StatesGroup):
    service = State()
    date = State()


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Привет! На какую услугу записать?")
    await state.set_state(Booking.service)


@dp.message(Booking.service)
async def choose_service(message: Message, state: FSMContext):
    await state.update_data(service=message.text)
    await message.answer("На какую дату записать?")
    await state.set_state(Booking.date)


@dp.message(Booking.date)
async def choose_date(message: Message, state: FSMContext):
    data = await state.get_data()
    service = data["service"]
    date = message.text

    await message.answer(
        f"Проверь запись:\nУслуга: {service}\nДата: {date}"
    )
    await state.clear()


@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Запись отменена. Напиши /start, чтобы начать заново.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
