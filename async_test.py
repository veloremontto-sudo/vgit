import asyncio
import time

def sync_task():
    print("Начало синхронной задачи")
    time.sleep(2)
    print("Конец синхронной задачи")

async def async_task():
    print("Начало асинхронной задачи")
    await asyncio.sleep(2)
    print("Конец асинхронной задачи")

async def main():
    print("--- Старт программы ---")

    await asyncio.gather(
        async_task(),
        async_task()
    )

    print("--- Финиш программы ---")

asyncio.run(main())