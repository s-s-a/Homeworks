import asyncio

# 1. Объявляем главную корутину
async def main():
    print("Hello...")
    # Здесь могла бы быть долгая операция, но пока мы просто подождем 1 секунду
    await asyncio.sleep(1)
    print("...async world!")

# 2. Запускаем программу с помощью asyncio.run()
# Эта функция создает event loop, выполняет нашу корутину main
# и закрывает loop после завершения.
print("Запускаем программу")
asyncio.run(main())
print("Программа завершена")