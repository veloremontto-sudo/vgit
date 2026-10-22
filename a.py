import asyncio
import time

async def process_order(client_name, seconds):
    print(f"Начат заказ для {client_name}...")
    await asyncio.sleep(seconds)
    print(f"Заказ для {client_name} готов!")

async def main():
    start_time = time.time()

    print("--- Мастерская открылась ---")

    await asyncio.gather(
        process_order("Анна", 2),
        process_order("Олег", 3),
        process_order("Мария", 1)
    )

    end_time = time.time()
    print(f"--- Мастерская закрылась. Общее время: {end_time - start_time:.2f} сек. ---")

asyncio.run(main())