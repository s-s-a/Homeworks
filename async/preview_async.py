"""_summary_
Запрос 3-х URL в aсинхронном режиме
"""

import aiohttp
import asyncio
import time

# Те же URL-адреса
urls = [
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/2',
]

async def fetch_async(session, url):
    """Асинхронно выполняет запрос к URL."""
    print(f"Запрашиваю {url}...")
    async with session.get(url) as response:
        await response.text()
        print(f"Запрос к {url} завершен.")

async def main():
    """Основная асинхронная функция."""
    async with aiohttp.ClientSession() as session:
        # Создаем список задач для одновременного выполнения
        tasks = [fetch_async(session, url) for url in urls]
        # Запускаем задачи и ждем их завершения
        await asyncio.gather(*tasks)

start_time = time.time()

# Запускаем выполнение асинхронной программы
asyncio.run(main())

end_time = time.time()

print(f"\nАсинхронное выполнение заняло: {end_time - start_time:.2f} секунд.")