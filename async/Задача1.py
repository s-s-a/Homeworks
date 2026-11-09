import asyncio


async def countdown(name: str, n: int):
    # print(f"{name} начал отсчет с {n}")
    while n > 0:
        print(f"{n}")
        n -= 1
        await asyncio.sleep(1)
    print(f"{name} : Пуск!")


# 1. Объявляем главную корутину
async def main():
    # Здесь могла бы быть долгая операция, но пока мы просто подождем 1 секунду
    await countdown("Таймер 1", 3)
    # await asyncio.sleep(1)


# 2. Запускаем программу с помощью asyncio.run()
# Эта функция создает event loop, выполняет нашу корутину main
# и закрывает loop после завершения.
print("Запускаем программу")
asyncio.run(main())
print("Программа завершена")
