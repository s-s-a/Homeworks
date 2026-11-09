import asyncio


async def racer(name: str, delay: float):
    await asyncio.sleep(delay)
    print(f"{name} финишировал!")

# 1. Объявляем главную корутину
async def main():
    Молния = asyncio.create_task(racer("Молния", 2))
    Стрела = asyncio.create_task(racer("Стрела", 2.5))
    await asyncio.gather(Молния, Стрела)


# 2. Запускаем программу с помощью asyncio.run()
# Эта функция создает event loop, выполняет нашу корутину main
# и закрывает loop после завершения.
print("Запускаем программу")
asyncio.run(main())
print("Программа завершена")