import asyncio

import aiohttp

urls = [
    "https://www.python.org",
    "https://www.google.com",
    "https://non-existent-domain-12345.org",
]


async def check_status(session, url: str):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"Сайт {url}: Ok")
    except:  # noqa: E722
        print(f"Сайт {url}: Не удалось подключиться")


# 1. Объявляем главную корутину
async def main():
    async with aiohttp.ClientSession() as session:
        # Создаем список задач для одновременного выполнения
        tasks = [check_status(session, url) for url in urls]
        # Запускаем задачи и ждем их завершения
        await asyncio.gather(*tasks)


# 2. Запускаем программу с помощью asyncio.run()
# Эта функция создает event loop, выполняет нашу корутину main
# и закрывает loop после завершения.
print("Запускаем программу")
asyncio.run(main())
print("Программа завершена")
